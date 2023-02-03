# SMART Health Card Terminology Scripts

## Setup

Requires Python 3.

1. Install [`pipenv`](https://pipenv.pypa.io/en/latest/index.html)
2. Run `pipenv install`

## Running

Run scripts with `pipenv run python3 script_folder/script_name_here.py`

## Tests

We use [`pytest`](https://docs.pytest.org). To run the test suite:

    pipenv run pytest

## Directory of scripts

### `lab_loinc/lab_loinc_covid.py`

This generates a ValueSet of LOINCs for qualitative COVID-related lab tests. It scrapes <https://loinc.org/sars-cov-2-and-covid-19/> for a list of all COVID lab test LOINCs, and then filters based on the answer lists employed by the LOINCs.

The `lab_loinc/lab_loinc_covid.yaml` file is an allow/deny-list of LOINC answer lists. Any lab test using an answer list that appears on the allow list will be included in the ValueSet, and any lab test using an answer list that appears on the deny list will be excluded.

The script will raise an exception if a LOINC has answer lists on both allow and deny lists, or if a LOINC uses an answer list that is not in `lab_loinc/lab_loinc_covid.yaml`.

If the `.fsh` file changes, the version will automatically be incremented. Versions are in `YYYY.n` format.