from lab_loinc_covid import *
import pytest

def test_get_covid_loincs_from_website():
    df = get_covid_loincs_from_website()
    assert df['LOINC_NUM'].eq('98069-8').any()
    assert df.shape[0] > 100  # More than 100 rows


def test_get_answer_list_codes_for_loinc():
    assert 'LL2021-5' in get_answer_list_codes_for_loinc('98069-8')

def test_increment_version():
    current_year = int(datetime.now().strftime("%Y"))

    assert increment_version(f'{current_year}.1') == f'{current_year}.2'
    assert increment_version(f'{current_year-1}.2') == f'{current_year}.1'
    assert increment_version(f'{current_year}.99') == f'{current_year}.100'
    assert increment_version(f'0.0') == f'{current_year}.1'
    assert increment_version(f'0.0.0') == f'{current_year}.1'

    with pytest.raises(BaseException) as e_info:
        increment_version('1.0')
    assert str(e_info.value) == '1.0 not in YYYY.n format'


class TestLoincAnswerList:
    TEST_CODE = 'LL2021-5'

    def test_fhir_lookup(self):
        answer_list = LoincAnswerList(TestLoincAnswerList.TEST_CODE)
        assert answer_list.fhir_lookup['resourceType'] == "Bundle"

    def test_name(self):
        answer_list = LoincAnswerList(TestLoincAnswerList.TEST_CODE)
        assert answer_list.name == 'Pos|Neg|Invalid'

    def test_answers(self):
        expected = [('LA15841-2', 'Invalid'), ('LA6576-8', 'Positive'), ('LA6577-6', 'Negative')]
        answer_list = LoincAnswerList(TestLoincAnswerList.TEST_CODE)

        for e in expected:
            assert e in answer_list.answers

        assert len(expected) == len(answer_list.answers)

    def test_loinc_snomed_answer_list_crosswalk_lookup(self):
        answer_list = LoincAnswerList(TestLoincAnswerList.TEST_CODE)
        df = answer_list.loinc_snomed_answer_list_crosswalk_lookup
        assert df['Answer ID'].isin(['LA6576-8']).any()
        assert (df[df['Answer ID'] == 'LA6576-8']['snomed_code'] == "10828004").all()
        assert (df[df['Answer ID'] == 'LA6576-8']['snomed_display'] == "Positive (qualifier value)").all()
        assert (df[df['Answer ID'] == 'LA6576-8']['loinc_answer'] == "Positive").all()

    def test_to_df(self):
        answer_list = LoincAnswerList(TestLoincAnswerList.TEST_CODE)
        df = answer_list.to_df()
        assert df.to_dict() == {
            'answer_list_code': {
                0: 'LL2021-5',
                1: 'LL2021-5',
                2: 'LL2021-5'
            },
            'answer_list_name': {
                0: 'Pos|Neg|Invalid',
                1: 'Pos|Neg|Invalid',
                2: 'Pos|Neg|Invalid'
            },
            'answer_loinc_code': {
                0: 'LA15841-2',
                1: 'LA6576-8',
                2: 'LA6577-6'
            },
            'answer_loinc_display': {
                0: 'Invalid',
                1: 'Positive',
                2: 'Negative'
            },
            'snomed_code': {
                0: '455371000124106',
                1: '10828004',
                2: '260385009'
            },
            'snomed_display': {
                0: 'Invalid result (qualifier value)',
                1: 'Positive (qualifier value)',
                2: 'Negative (qualifier value)'
            }
        }
