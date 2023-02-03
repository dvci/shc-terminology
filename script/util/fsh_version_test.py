import pytest

from util.fsh_version import *

fsh = '''
ValueSet: QualitativeCovidLabTestValueSet
Id: qualitative-covid-lab-test
Title: "LOINCs identifying qualitative COVID lab tests"
Description: "This value set includes a subset of the LOINCs found at <https://loinc.org/sars-cov-2-and-covid-19/> that identify COVID-19-related laboratory tests. Only those laboratory tests that include qualitative results we believe to be useful in SMART Health Cards are included."


* ^copyright = "This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2022, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc"
* ^version = "2022.2"


* $loinc#94307-6 "SARS-CoV-2 N gene Spec Ql NAA N1"
* $loinc#94308-4 "SARS-CoV-2 N gene Spec Ql NAA N2"
'''


def test_get_old_version():
    assert get_old_version(fsh) == "2022.2"


def test_increment_version():
    current_year = int(datetime.datetime.now().strftime("%Y"))

    assert increment_version(f'{current_year}.1') == f'{current_year}.2'
    assert increment_version(f'{current_year-1}.2') == f'{current_year}.1'
    assert increment_version(f'{current_year}.99') == f'{current_year}.100'
    assert increment_version(f'0.0') == f'{current_year}.1'
    assert increment_version(f'0.0.0') == f'{current_year}.1'

    with pytest.raises(BaseException) as e_info:
        increment_version('1.0')
    assert str(e_info.value) == '1.0 not in YYYY.n format'


def test_update_version():
    assert f'{datetime.datetime.now().strftime("%Y")}.1' in update_version(fsh, '2022.2')
