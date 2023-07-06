import datetime as dt
import json
import logging
import os

import numpy as np
import pandas as pd
import requests
import yaml


def retrieve_new_cvx():
    '''
    use requests.get to retrieve latest flat file from CDC
    saves the file as newest_cvx_file for posterity and returns file for reading
    '''
    CVX = 'https://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/cvx.txt'

    # retrieve flat file data
    response = requests.get(CVX)

    response.encoding = 'utf-8'

    with open('cvx_cdc.txt', 'w') as outfile:
        outfile.write(response.text)

    # Convert .txt file to dict where keys are CVX codes and values are a dict of metadata for that code
    df = pd.read_csv('cvx_cdc.txt', sep='|', names=[
        'short-description',
        'full-vaccine-name',
        'notes',
        'vaccine-status',
        'nonvaccine',
        'last-update-date',
    ])
    return df.to_dict(orient='index')


def filter_cvx(new_cvx, terms):
    out = {}

    for cvx, data in new_cvx.items():
        for term in terms:
            if (term.lower() in data['short-description'].lower()) or (term.lower() in data['full-vaccine-name'].lower()):
                out[cvx] = data
                break

    return out


def retrieve_new_cvx_product_names():
    '''
    use requests.get to retrieve latest trade name flat file from CDC
    saves the file and returns for reading
    '''
    PRODUCT = 'https://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/TRADENAME.txt'

    # retrieve flat file data
    response = requests.get(PRODUCT)

    # extract content and write to a file
    with open('name_cdc.txt', 'w') as outfile:
        outfile.write(response.text)

    df = pd.read_csv('name_cdc.txt', sep='|', index_col=False, names=[
        'prod-name',
        'short-description',
        'cvx-code',
        'manufacturer-name',
        'mvx-code',
        'mvx-status',
        'product-name-status',
        'last-update-date'
    ])

    # Removing filter by disease for now -- can add back in later if necessary
    # Filter to just diseases of interest
    # of_interest = ['covid', 'monkeypox', 'smallpox']

    # Find rows that contain the disease name of interest, based on https://stackoverflow.com/a/43018248
    # filter = np.any([df.apply(lambda r: r.str.contains(s, case=False).any(), axis=1) for s in of_interest], 0)

    # Only include non-blank product names
    f = np.all([df['prod-name'].notnull(), (df['prod-name'] != '')], 0)

    # Only include active product names
    df_filtered = df[f & (df['product-name-status'] == 'Active')]

    # If there are duplicate CVX x product-name combinations, choose the one with the most recent `last-update-date`
    # Then spit out a dict where the key is the CVX code and the value is the product name.
    return df_filtered \
        .sort_values(by=['cvx-code', 'last-update-date']) \
        .drop_duplicates(subset=['cvx-code'], keep='last', ignore_index=True) \
        .set_index('cvx-code')['prod-name'].to_dict()


def read_value_set(filename):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, f'../../input/vocabulary/{filename}')

    with open(filename, 'r') as f:
        return json.load(f)


def write_value_set(filename, value_set):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, f'../../input/vocabulary/{filename}')

    with open(filename, 'w') as f:
        f.write(json.dumps(value_set, indent=2))


def read_excluded_cvx():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'cvx_exclude.yaml')

    with open(filename, "r") as f:
        return yaml.safe_load(f)


def cvx_product_name(cvx_code, new_cvx, cvx_product_names):
    return cvx_product_names[cvx_code] if cvx_code in cvx_product_names else new_cvx[cvx_code][
        'short-description']


def update_value_set(value_set, new_cvx, cvx_product_names):
    '''
    update the covid-cvx.json vocab file with all
    COVID-19 vaccines
    '''

    # CVX codes are strings in the ValueSet, so make sure we are working with strings everywhere
    new_cvx = {str(k): v for k, v in new_cvx.items()}
    cvx_product_names = {str(k): v for k, v in cvx_product_names.items()}

    # Remove manually excluded CVX
    excluded = read_excluded_cvx()
    logging.info(f'{len(excluded)} CVX code(s) manually excluded in cvx_exclude.yaml')
    logging.info(f'{len(new_cvx)} CVX code(s) before applying exclusion')
    new_cvx = {k: v for k, v in new_cvx.items() if k not in excluded}
    logging.info(f'{len(new_cvx)} CVX code(s) after applying exclusion')

    # Pull out CVX codes already in the ValueSet for convenience
    existing_concepts = value_set['compose']['include'][0]['concept']
    current_cvx_codes = [str(c['code']) for c in existing_concepts]

    # Find CVX codes in the `cvx` dict that are already in the value set
    cvx_already_included = [c for c in new_cvx.keys() if c in current_cvx_codes]

    # Find CVX codes that are in the `cvx` dict and are **brand new** to the value set
    cvx_to_add = [c for c in new_cvx.keys() if c not in cvx_already_included]

    # Logging
    logging.info(f'{len(current_cvx_codes)} CVX code(s) currently in the value set')
    logging.info(f'{len(new_cvx)} CVX code(s) in the canonical list of CVX for inclusion, {len(cvx_already_included)} of which are already in the value set')
    logging.info(f'{len(cvx_to_add)} CVX code(s) to be added to the value set')

    # Add the new CVX codes to the value set
    for cvx_code in cvx_to_add:
        product_name = cvx_product_name(cvx_code, new_cvx, cvx_product_names)
        logging.info(f'  Adding CVX {cvx_code} <{product_name}> to the value set')
        value_set['compose']['include'][0]['concept'].append(
            {
                "code": str(cvx_code),
                "display": new_cvx[cvx_code]['short-description'],
                "designation": [
                    {
                        "language": "en-US",
                        "use": {
                            "system": "https://terminology.smarthealth.cards/CodeSystem/designation-use",
                            "use": "consumer-friendly"
                        },
                        "value": product_name
                    }
                ]
            }
        )

    # Sort the `concept` contents by `code`
    value_set['compose']['include'][0]['concept'] = sorted(
        value_set['compose']['include'][0]['concept'],
        key=lambda x: x['code']
    )

    # Update display of existing CVX codes -- this should always be the official short display of the code system
    for cvx_code in cvx_already_included:
        # `i` is the index of this CVX code within the concept element
        i, existing_concept = [(i, c) for i, c in enumerate(value_set['compose']['include'][0]['concept']) if c['code'] == cvx_code][0]
        value_set['compose']['include'][0]['concept'][i]['display'] = new_cvx[cvx_code]['short-description']

        # If a `en-US` designation is missing, add one
        if ('designation' not in (value_set['compose']['include'][0]['concept'][i])):
            value_set['compose']['include'][0]['concept'][i]['designation'] = []

        if not [d for d in value_set['compose']['include'][0]['concept'][i]['designation'] if d['language'] == 'en-US']:
            value_set['compose']['include'][0]['concept'][i]['designation'].append({
                "language": "en-US",
                "use": {
                    "system": "https://terminology.smarthealth.cards/CodeSystem/designation-use",
                    "use": "consumer-friendly"
                },
                "value": cvx_product_name(cvx_code, new_cvx, cvx_product_names)
            })

    return value_set


def main():
    logging.basicConfig(encoding='utf-8', level=logging.INFO)

    # COVID
    logging.info("\n\nBeginning COVID")
    COVID_VALUE_SET = 'immunization-covid-cvx.json'

    # Retrieve newest CVX file from CDC
    new_cvx = retrieve_new_cvx()

    # Filter to just COVID-related
    new_cvx = filter_cvx(new_cvx, ['covid'])

    # Retrieve newest product name file from CDC
    cvx_product_names = retrieve_new_cvx_product_names()

    # Load in existing value set
    value_set = read_value_set(COVID_VALUE_SET)

    # Update value set
    value_set = update_value_set(value_set, new_cvx, cvx_product_names)
    write_value_set(COVID_VALUE_SET, value_set)


    # Mpx/Smallpox
    logging.info("\n\nBeginning mpx")
    COVID_VALUE_SET = 'immunization-orthopoxvirus-cvx.json'

    # Retrieve newest CVX file from CDC
    new_cvx = retrieve_new_cvx()

    # Filter to just COVID-related
    new_cvx = filter_cvx(new_cvx, ['monkeypox', 'smallpox'])

    # Retrieve newest product name file from CDC
    cvx_product_names = retrieve_new_cvx_product_names()

    # Load in existing value set
    value_set = read_value_set(COVID_VALUE_SET)

    # Update value set
    value_set = update_value_set(value_set, new_cvx, cvx_product_names)
    write_value_set(COVID_VALUE_SET, value_set)

    # All CVX ValueSet
    logging.info("\n\nBeginning all CVX")
    out = f"""//
//
// WARNING!
// This file is automatically generated by `/script/cvx/cvx_parsing.py`. Do not manually edit.
//
//
Alias: $cvx = http://hl7.org/fhir/sid/cvx

ValueSet: ImmunizationAllCvxValueSet
Id: immunization-all-cvx
Title: "Immunization / All / CVX"
Description: "Contains all CVX codes from <https://www2.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx> as of {dt.datetime.now().strftime('%Y-%m-%d')}."

* ^copyright = ""

* ^version = "{dt.datetime.now().strftime('%Y%m%d')}"

"""

    for code, data in retrieve_new_cvx().items():
        out += f'* $cvx#{code} "{data["short-description"]}"\n'

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, f'../../input/fsh/immunization-all-cvx.fsh')

    with open(filename, 'w') as f:
        f.write(out)


if __name__ == "__main__":
    main()
