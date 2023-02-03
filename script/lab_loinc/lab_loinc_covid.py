from datetime import datetime
import os
from itertools import chain
import json


import pandas as pd
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import yaml
# noinspection PyUnresolvedReferences
import json_fix  # Used to make a custom object serializable by JSON.dump

import sys
sys.path.append(os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))
from util.fsh_version import get_old_version, update_version

LOINC_COVID_URL = 'https://loinc.org/sars-cov-2-and-covid-19/'

class LoincAnswerList:
    """Represents a LOINC Answer List"""

    def __init__(self, code):
        self.code = code

        self._name = None
        self._answers = None
        self._fhir_lookup = None
        self._loinc_snomed_crosswalk_lookup = None
        self._df = None

    @property
    def name(self) -> str:
        if self._name is None:
            names = pd.Series([entry['resource']['name'] for entry in self.fhir_lookup['entry']]).unique().tolist()

            if len(names) > 1:
                raise BaseException(f"Multiple names for {self.code}")

            self._name = names[0]

        return self._name

    @property
    def answers(self) -> list[tuple]:
        """Gets answer list codes from LOINC

        Flattens all LOINC versions down

        Returns:
            list: list of unique tuples like ("LAXXXX-X", "Display text")

        """
        if self._answers is None:
            # Extract the objects holding the included codes
            included_codes = [e['resource']['compose']['include'] for e in self.fhir_lookup['entry']]

            # Flatten down so they can all be processed
            included_codes = list(chain(*included_codes))
            included_codes = [c['concept'] for c in included_codes]
            included_codes = list(chain(*included_codes))

            # Get unique answer codes
            unique = list(set([c['code'] for c in included_codes]))

            # Get *all* display names for each code, newline delimited
            display = ["\n".join(set([c['display'] for c in included_codes if c['code'] == u])) for u in unique]

            # Print out any codes with multiple names
            for i, u in enumerate(unique):
                if '\n' in display[i]:
                    out = '\n'.join([f'      {d}' for d in display[i].split('\n')])
                    print(f"    {u} has multiple display names:\n{out}")

            self._answers = list(zip(unique, display))

        return self._answers

    @property
    def fhir_lookup(self) -> dict:
        if self._fhir_lookup is None:
            load_dotenv()

            url = f'https://fhir.loinc.org/ValueSet/?url=http://loinc.org/vs/{self.code}'

            resp = requests.get(url, auth=HTTPBasicAuth(username=os.environ.get('LOINC_USERNAME'),
                                                        password=os.environ.get('LOINC_PASSWORD')))
            self._fhir_lookup = resp.json()

        return self._fhir_lookup

    @property
    def loinc_snomed_answer_list_crosswalk_lookup(self) -> pd.DataFrame:
        if self._loinc_snomed_crosswalk_lookup is None:
            dfs = pd.read_html(f'https://loinc.org/{self.code}/')
            df = dfs[0]
            df = df.join(
                df['Answer'].str.extract(
                    '(?P<loinc_answer>.*) Copyright http://snomed.info/sct ID:(?P<snomed_code>[0-9]+) ('
                    '?P<snomed_display>.*)',
                    expand=True)
            )

            self._loinc_snomed_crosswalk_lookup = df
        return self._loinc_snomed_crosswalk_lookup


    def to_df(self) -> pd.DataFrame:
        if self._df is None:
            colnames = [
                'answer_list_code',
                'answer_list_name',
                'answer_loinc_code',
                'answer_loinc_display',
                'snomed_code',
                'snomed_display'
            ]
            self._df = pd.DataFrame(self.answers, columns=colnames[2:4])
            self._df[colnames[0]] = self.code
            self._df[colnames[1]] = self.name
            self._df = self._df.merge(
                self.loinc_snomed_answer_list_crosswalk_lookup[['Answer ID', 'snomed_code', 'snomed_display']],
                how='left',
                left_on='answer_loinc_code',
                right_on='Answer ID'
            ).sort_values(by=['answer_loinc_code'], ignore_index=True)
            self._df = self._df[colnames]

        return self._df[colnames]

    def __json__(self):
        return self.answers


def get_covid_loincs_from_website() -> list[pd.DataFrame]:
    dfs = pd.read_html(LOINC_COVID_URL)
    return dfs[0]


def get_answer_list_codes_for_loinc(loinc) -> list[str]:
    load_dotenv()

    url = f'https://fhir.loinc.org/CodeSystem/$lookup?system=http://loinc.org&code={loinc}'

    resp = requests.get(url, auth=HTTPBasicAuth(username=os.environ.get('LOINC_USERNAME'),
                                                password=os.environ.get('LOINC_PASSWORD')))
    code_system = resp.json()

    # Extract the `answer-list` code from the JSON response -- this is kind of gross, but it works
    return [p['part'][1]['valueString'] for p in code_system['parameter'] if
            'part' in p and 'valueCode' in p['part'][0] and p['part'][0]['valueCode'] == 'answer-list']

def main():
    dirname = os.path.dirname(__file__)

    # Get all COVID lab tests from loinc.org
    all_lab_tests = get_covid_loincs_from_website()

    # For each lab test, get the answer list
    answer_lists = {}
    answer_lists_for_loinc = {}
    for loinc in all_lab_tests['LOINC_NUM']:
        print(f'Processing LOINC {loinc}...', end='')
        answer_lists_for_loinc[loinc] = get_answer_list_codes_for_loinc(loinc)

        for answer_list_code in answer_lists_for_loinc[loinc]:
            if answer_list_code not in answer_lists:
                print(f'\n  Loading answer list {answer_list_code}...', end='')
                answer_lists[answer_list_code] = LoincAnswerList(answer_list_code)
                print('done.')
        print(f'done.')
    print('\n\n', f'{len(answer_lists_for_loinc)} COVID LOINCs found')
    print(f'These use {len(answer_lists)} unique answer lists', '\n')

    # Dump out all answer lists into CSV for manual analysis
    df = pd.concat([a.to_df() for a in answer_lists.values()])
    df.to_csv(os.path.join(dirname, 'answer_lists.csv'))

    # Filter lab tests to just those that use the approved answer lists
    with open(os.path.join(dirname, 'lab_loinc_covid.yaml'), 'r') as file:
        prescreened_answer_lists = yaml.safe_load(file)

    # `answer_lists_for_loinc` has the LOINC as the key, and a list of answer lists as the value
    # Use set intersections to concisely get the LOINCs that use answer lists that are in are pre-screened
    # "included" list:
    included_lab_tests = {k:v for (k, v) in answer_lists_for_loinc.items() if len(set(prescreened_answer_lists['included']).intersection(set(v))) > 0}.keys()

    # Same thing but for the "excluded" list of answer sets:
    ignored_lab_tests = {k:v for (k, v) in answer_lists_for_loinc.items() if len(set(prescreened_answer_lists['ignored']).intersection(set(v))) > 0}.keys()

    # Raise an exception if there are LOINCs in both the included and excluded lists:
    if len(set(included_lab_tests).intersection(set(ignored_lab_tests))) > 0:
        print("Some LOINCs are both included and excluded based on the pre-screened answer lists:")
        print(set(included_lab_tests).intersection(set(ignored_lab_tests)))
        raise BaseException("LOINCs are both included and excluded")

    # Raise an exception for new answer lists not in the prescreen
    new_answer_lists = [a for a in answer_lists.keys() if a not in prescreened_answer_lists['included'] and a not in prescreened_answer_lists['ignored']]
    if len(new_answer_lists) > 0:
        print("\n\n\nLOINC answer lists not found in `lab_loinc_covid.yaml`:")
        print(json.dumps({k:v for (k, v) in answer_lists.items() if k in new_answer_lists}, indent=2))
        raise BaseException("New LOINC answer lists that are not in the `lab_loinc_covid.yaml` file - see above.")

    # Get the display names of the LOINCs in a dict like {'12345-6': 'display name'}
    loinc_display_names = dict(zip(*all_lab_tests[['LOINC_NUM','Shortname']].to_dict(orient='list').values()))

    # Read version from existing .fsh file
    fsh_path = os.path.join(dirname, '../../input/fsh/covid-lab-loinc.fsh')
    with open(fsh_path, 'r') as f:
        old_fsh = f.read()
    old_version = get_old_version(old_fsh)

    # Produce .fsh file for the COVID lab LOINCs that use the answer lists that make sense for our use case
    fsh_included_lab_tests = "\n".join(sorted([f'* $loinc#{l} "{loinc_display_names[l]}"' for l in included_lab_tests]))
    fsh = f'''//
//
// WARNING!
// This file is automatically generated by `/script/lab_loinc/lab_loinc_covid.py`. Do not manually edit.
//
//
Alias: $loinc = http://loinc.org

ValueSet: QualitativeCovidLabTestValueSet
Id: qualitative-covid-lab-test
Title: "LOINCs identifying qualitative COVID lab tests"
Description: "This value set includes a subset of the LOINCs found at <{LOINC_COVID_URL}> that identify COVID-19-related laboratory tests. Only those laboratory tests that include qualitative results we believe to be useful in SMART Health Cards are included."


* ^copyright = "This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2022, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc"
* ^version = "{old_version}"


{fsh_included_lab_tests}
'''

    intro = f'''### Usage

This value set includes a subset of the LOINCs found at <{LOINC_COVID_URL}> that identify COVID-19-related laboratory tests. Only those laboratory tests that include qualitative results we believe to be useful in SMART Health Cards are included.

The purpose of this value set is to provide Issuers guidance on what LOINCs Verifiers are likely to expect in a COVID-19-related SMART Health Card. It is possible to construct a fully valid SMART Health Card that identifies a laboratory test with a LOINC *not* in this list, but it may be less likely that a Verifier will have included such a LOINC in their logic for processing the SMART Health Card data.

This ValueSet is programmatically generated by [this script](https://github.com/dvci/shc-terminology/tree/main/script/lab_loinc/lab_loinc_covid.py).
'''

    # Check for changes to FSH, and if there are changes increment the version
    if fsh != old_fsh:
        fsh = update_version(fsh, old_version)

    # Write FSH to file
    with open(fsh_path, 'w') as f:
        f.write(fsh)

    filename = os.path.join(dirname, '../../input/pagecontent/ValueSet-qualitative-covid-lab-test-value-set-intro.md')
    with open(filename, 'w') as f:
        f.write(intro)


    # Create ValueSet of SNOMED codes for the lab results - these can be used not just for COVID but all qualitative
    # lab tests related to infectious diseases.
    with open(os.path.join(dirname, 'lab_loinc_snomed.yaml'), 'r') as file:
        loinc_snomed = yaml.safe_load(file)

    results_human_readable = '{:.table-striped.table.table-bordered}\n|SNOMED-CT|LOINC Answer|\n|-|-|'
    results_fsh = []
    for c in loinc_snomed:
        if c['snomed'] is not False:
            results_human_readable += f'\n|`{c["snomed"]}`<br>{c["snomed_display"]}|`{c["loinc"]}`<br>{c["loinc_display"]}|'
            results_fsh.append(f'* $snomed#{c["snomed"]} "{c["snomed_display"]}"')
        else:
            results_human_readable += f'\n|*No equivalent*|`{c["loinc"]}`<br>{c["loinc_display"]}|'
            results_fsh.append(f'* $loinc#{c["loinc"]} "{c["loinc_display"]}"')

    results_fsh.sort()
    results_fsh = '\n'.join(results_fsh)

    # Read version from existing .fsh file
    fsh_path = os.path.join(dirname, '../../input/fsh/lab-qualitative-results.fsh')
    with open(fsh_path, 'r') as f:
        old_fsh = f.read()
    old_version = get_old_version(old_fsh)

    fsh = f'''//
//
// WARNING!
// This file is automatically generated by `/script/lab_loinc/lab_loinc_covid.py`. Do not manually edit.
//
//
Alias: $snomed = http://snomed.info/sct
Alias: $loinc = http://loinc.org

ValueSet: QualitativeLabTestResultValueSet
Id: qualitative-lab-test-result
Title: "Qualitative infectious disease-related lab test result codes"
Description: "This value set includes a codes to identify the results of qualitative lab tests related to infectious diseases."

* ^copyright = "This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2022, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc

The SNOMED CT codes in this ValueSet are part of SNOMED GPS, which is produced by SNOMED International under the terms of the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/).

Additional information about this license specific to SNOMED International's release of the GPS:

- SNOMED CT is © and ® SNOMED International. The right to maintain the GPS remains vested exclusively in SNOMED International.
- The Licensee can redistribute the GPS.
- The Licensee can create derivatives or implementation-related products and services based on the GPS.
- The Licensee cannot claim that SNOMED International or any of its Members endorses the Licensee's derivative because it uses content from the GPS.
- Neither SNOMED International nor any of the contributors accept any liability for the Licensee's use or redistribution of the GPS.
- SNOMED CT® was originally created by the College of American Pathologists.

Without obtaining prior written permission from SNOMED International, you are expressly prohibited from using, distributing or reproducing the SNOMED International, SNOMED CT or SNOMED GPS logo, service mark or trademark. Please review all terms and conditions of use [here](http://www.snomed.org/terms-and-conditions)."

* ^version = "{old_version}"

{results_fsh}
'''

    # Check for changes to FSH, and if there are changes increment the version
    if fsh != old_fsh:
        fsh = update_version(fsh, old_version)

    # Write FSH to file
    with open(fsh_path, 'w') as f:
        f.write(fsh)


    intro = f'''### Usage

Use of SNOMED CT concepts for representing laboratory test results is preferred. For convenience, the table below provides equivalencies between SNOMED CT concepts and LOINC answers.

{results_human_readable}

This ValueSet is programmatically generated by [this script](https://github.com/dvci/shc-terminology/tree/main/script/lab_loinc/lab_loinc_covid.py).'''
    filename = os.path.join(dirname, '../../input/pagecontent/ValueSet-qualitative-lab-test-result-intro.md')
    with open(filename, 'w') as f:
        f.write(intro)

if __name__ == "__main__":
    main()
