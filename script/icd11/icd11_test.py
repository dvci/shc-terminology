from icd11 import *

fetcher = Icd11Fetcher()


def test_get_token():
    assert fetcher.get_token() is not ''
    assert fetcher.get_token() == fetcher.get_token()


def test_get_latest_release_for_entity():
    regex = r"\d{4}-\d{2}"
    latest = fetcher.get_latest_release_for_entity('164949870')
    assert re.match(regex, latest), "Latest release is in YYYY-MM format"


def test_get_mms_descendants_for_entity():
    covid19_rna_vaccines = '873941688'
    latest = fetcher.get_latest_release_for_entity(covid19_rna_vaccines)

    # XM3DT5 is the ICD-11 MMS code for the Moderna vaccine
    descendants = fetcher.get_mms_descendants_for_entity(covid19_rna_vaccines, latest)
    assert 'XM3DT5' in descendants
    assert descendants['XM3DT5'] == "COVID-19 Vaccine Moderna"
