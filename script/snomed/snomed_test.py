from snomed import *

def test_get_snomed_codes_from_url():
    url = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN%2F2022-05-31/concepts?ecl=%3C%3C%2028531000087107'

    # Get total expected number of codes
    response = requests.get(url, headers={'User-Agent': 'curl/7.79.1'})
    response_json = response.json()

    # Get codes using method using small limit to test paging
    codes = get_snomed_codes_from_url(url, limit=2, edition="Testing")

    assert len(codes) == response_json['total']
    assert '30141000087107' in [c['conceptId'] for c in codes]
    assert codes[0]['edition'] == 'Testing'

def test_get_covid19_vaccine_snomed_canada():
    codes = get_covid19_vaccine_snomed_canada()
    # 28571000087109 "COVID-19 SPIKEVAX mRNA Mod"
    assert '28571000087109' in [c['conceptId'] for c in codes]

def test_get_covid19_vaccine_snomed_belgium():
    codes = get_covid19_vaccine_snomed_belgium()
    # 10871000172106 "COVID-19 mRNA vaccine (mRNA-1273) of Moderna"
    assert '10871000172106' in [c['conceptId'] for c in codes]

def test_get_covid19_vaccine_snomed_argentina():
    codes = get_covid19_vaccine_snomed_argentina()
    # 424731000221108 "SPIKEVAX vacuna COVID-19 ARNm (producto medicinal comercial)"
    assert '424731000221108' in [c['conceptId'] for c in codes]

def test_get_covid19_vaccine_snomed_ireland():
    codes = get_covid19_vaccine_snomed_ireland()
    # 1421000220104 "COVID-19 mRNA Vaccine Moderna 0.1mg per 0.5mL dose dispersion for injection multidose vials"
    assert '1421000220104' in [c['conceptId'] for c in codes]

def test_get_covid19_vaccine_snomed_international():
    codes = get_snomed_covid19_vaccine_international()
    # 29061000087103 "COVID-19 non-replicating viral vector vaccine"
    assert '29061000087103' in [c['conceptId'] for c in codes]

def test_aggregate_covid19_vaccine_snomed_releases():
    codes = aggregate_covid19_vaccine_snomed_releases()

    assert '1421000220104' in [c['conceptId'] for c in codes]
    assert '29061000087103' not in [c['conceptId'] for c in codes]

def test_codes_to_df():
    codes = aggregate_covid19_vaccine_snomed_releases()

    df = codes_to_df(codes)

    assert df.columns.to_list() == ['SNOMED Code', 'Preferred term', 'Language', 'Edition', 'Active?']
    assert '28571000087109' in df['SNOMED Code'].to_list() # Canada Spikevax

def test_get_covid19_vaccine_snomed_uk():
    return None

    # WIP
    # Sample code from https://github.com/NHSDigital/TerminologyServer/blob/main/codesnippets/Content%20specific/SNOMED/ValueSet/expand/python/expand%20SNOMED%20ECL-based%20ValueSet%20(inline)
    import http.client
    import json

    conn = http.client.HTTPSConnection("ontology.nhs.uk")
    payload = json.dumps({
        "resourceType": "Parameters",
        "parameter": [
            {
                "name": "valueSet",
                "resource": {
                    "resourceType": "ValueSet",
                    "compose": {
                        "include": [
                            {
                                "system": "http://snomed.info/sct",
                                "filter": [
                                    {
                                        "property": "constraint",
                                        "op": "=",
                                        "value": "<< 39330711000001103"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        ]
    })
    headers = {
        'Content-Type': 'application/fhir+json',
        'Authorization': 'Bearer <token>'
    }
    conn.request("POST", "/production1/fhir/ValueSet/$expand", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
