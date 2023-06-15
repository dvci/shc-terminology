import os

import pandas as pd
import requests

import sys
sys.path.append(os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))
from util.fsh_version import get_old_version, update_version

IG_TABLE_CLASS = '{:.table-striped.table.table-bordered}'

def get_snomed_codes_from_url(url, limit=50, offset=0, edition=None, language=None):
    if 'offset=' in url or 'limit=' in url:
        raise BaseException('Cannot specify offset or limit params in URL directly')

    # SNOMED API gets cranky without specifying a user agent
    headers = {'User-Agent': 'curl/7.79.1'}
    if language is not None:
        headers['Accept-Language'] = language

    response = requests.get(url, params={'limit': limit, 'offset': offset}, headers=headers)
    response_json = response.json()

    # Add "edition" element
    for i, _ in enumerate(response_json['items']):
        response_json['items'][i]['edition'] = edition

    if response_json['offset'] + len(response_json['items']) < response_json['total']:
        return response_json['items'] + get_snomed_codes_from_url(
            url, limit=limit, offset=offset + limit, edition=edition, language=language
        )

    return response_json['items']


def get_covid19_vaccine_snomed_canada():
    url = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN/SNOMEDCT-CA/concepts?ecl=%3C%3C%2028531000087107'
    return get_snomed_codes_from_url(url, edition="Canadian")


def get_covid19_vaccine_snomed_belgium():
    url = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN/SNOMEDCT-BE/concepts?ecl=%3C%3C%2028531000087107'
    return get_snomed_codes_from_url(url, edition="Belgian")


def get_covid19_vaccine_snomed_argentina():
    url = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN/SNOMEDCT-ES/SNOMEDCT-AR/concepts?ecl=%3C%3C%2028531000087107'
    return get_snomed_codes_from_url(url, edition="Argentinian", language='es')


def get_covid19_vaccine_snomed_ireland():
    # Note that this is just the 787859002 "Vaccine product" root code -- need to do further filtering for COVID-19
    url = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN/SNOMEDCT-IE/concepts?ecl=%3C%3C%20787859002'
    codes = get_snomed_codes_from_url(url, edition="Irish")

    return [c for c in codes if 'COVID-19' in c['fsn']['term']]


def get_snomed_covid19_vaccine_international():
    url = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN/concepts?ecl=%3C%3C%2028531000087107'
    return get_snomed_codes_from_url(url, edition="International")


def get_infectious_diseases_vaccine_international():
    url = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN/concepts?ecl=%3C%3C%2040733004'
    return get_snomed_codes_from_url(url, edition="International")

def aggregate_covid19_vaccine_snomed_releases():
    """Combines the various national editions into a single list, and removes the non-specific int'l edition vaccine codes"""

    # TODO need to add UK codes once we verify it's ok to create a system-to-system account
    codes = get_covid19_vaccine_snomed_canada() + get_covid19_vaccine_snomed_belgium() + get_covid19_vaccine_snomed_ireland() + get_covid19_vaccine_snomed_argentina()
    print(f'{len(codes)} codes found.')

# Exclude non-specific int'l codes for COVID vaccines
    excluded_codes = get_snomed_covid19_vaccine_international()

    codes = [c for c in codes if c['conceptId'] not in [d['conceptId'] for d in excluded_codes]]

    return codes


def codes_to_df(codes):

    codes_for_df = [{
        "SNOMED Code": c['conceptId'],
        "Preferred term": c['pt']['term'],
        "Language": c['pt']['lang'],
        "Edition": c['edition'],
        "Active?": c['active']
    } for c in codes]

    return pd.DataFrame(codes_for_df).sort_values(['Edition', 'Active?', 'SNOMED Code'])


def get_covid19_vaccine_intro(df):
    return f'''### Usage
    
Implementers SHOULD use one of the SNOMED CT codes listed below when identifying a COVID-19 vaccine with a SNOMED CT code:

{IG_TABLE_CLASS}
{df.to_markdown(index=False)}
    
This ValueSet is programmatically generated by [this script](https://github.com/dvci/shc-terminology/tree/main/script/snomed/snomed.py).
'''


def get_covid19_vaccine_fsh(codes, version):
    codes = "\n".join([f'* $snomed#{c["conceptId"]} "{c["pt"]["term"]}"' for c in sorted(codes, key=lambda d: d['conceptId'])])
    return f'''//
//
// WARNING!
// This file is automatically generated by `/script/snomed/snomed.py`. Do not manually edit.
//
//
Alias: $snomed = http://snomed.info/sct

ValueSet: ImmunizationCovidSnomedValueSet
Id: immunization-covid-snomed
Title: "Immunization / COVID / SNOMED CT"
Description: "Contains SNOMED CT codes that identify specific COVID-19 vaccines for use in SMART Health Cards."

* ^copyright = "© 2021 International Health Terminology Standards Development Organisation. All rights reserved. SNOMED CT® was originally created by the College of American Pathologists.
* ^version = "{version}"

The SNOMED-CT® concepts in this ValueSet are produced by SNOMED International under the terms of the Creative Commons Attribution 4.0 International Public License."

{codes}
'''


def main():
    codes = aggregate_covid19_vaccine_snomed_releases()
    df = codes_to_df(codes)

    dirname = os.path.dirname(__file__)

    # Write FSH
    filename = os.path.join(dirname, '../../input/fsh/immunization-covid-snomed.fsh')

    # Get current file to determine version
    with open(filename, 'r') as f:
        old_fsh = f.read()
    old_version = get_old_version(old_fsh)
    print(f'Old version was {old_version}')

    # Generate new FSH, check to see if it has changed, and increment version if it has
    new_fsh = get_covid19_vaccine_fsh(codes, old_version)
    if old_fsh != new_fsh:
        print(f'Changes detected!')
        new_fsh = update_version(new_fsh, old_version)
        print(f'New version: {get_old_version(new_fsh)}')

    # Write new FSH to file
    with open(filename, 'w') as f:
        f.write(new_fsh)

    # Write intro Markdown to file
    filename = os.path.join(dirname, '../../input/pagecontent/ValueSet-immunization-covid-snomed-intro.md')
    with open(filename, 'w') as f:
        f.write(get_covid19_vaccine_intro(df))


if __name__ == "__main__":
    main()
