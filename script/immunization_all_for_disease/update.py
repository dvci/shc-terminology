import os
import datetime as dt
import json

source_files = {
    'COVID': [
        'input/vocabulary/immunization-covid-cvx.json',
        'fsh-generated/resources/ValueSet-immunization-covid-snomed.json',
        'fsh-generated/resources/ValueSet-immunization-covid-icd11.json',
    ],
    'orthopoxvirus': ['input/vocabulary/immunization-orthopoxvirus-cvx.json']
}

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

for disease, sources in source_files.items():
    # Convert source file paths to URLs in the published IG
    urls = []
    for s in sources:
        if s.startswith('fsh-generated'):
            urls.append(s.replace('fsh-generated/resources/', ''))
        else:
            urls.append(s.replace('input/vocabulary/', 'ValueSet-'))
    semicolon_list = '; '.join([f'<a href="{u.replace(".json", ".html")}">{u}</a>' for u in urls])

    out = {
        "resourceType": "ValueSet",
        "id": f"immunization-{disease.lower()}-all",
        "language": "en",
        "url": f"https://terminology.smarthealth.cards/ValueSet/immunization-{disease.lower()}-all",
        "version": dt.datetime.today().strftime('%Y%m%d'),
        "name": f"Immunization{disease.title()}AllValueSet",
        "title": f"Immunization / {disease} / All codes",
        "date": dt.datetime.today().strftime('%Y-%m-%d'),
        "status": "active",
        "publisher": "terminology.smarthealth.cards",
        "contact": [
            {
                "name": "SMART Health Cards",
                "telecom": [
                    {
                        "system": "email",
                        "value": "vci-ig@mitre.org"
                    }
                ]
            }
        ],
        "description": f"A list of all immunization codes for {disease}, combining the following ValueSets: {semicolon_list}",
        "copyright": f"Please see the following links for the copyright/legal information for each code system included here: {semicolon_list}",
        "compose": {
            "include": []
        }
    }
    for source_path in sources:
        # Assumes that each .json file does not include codes from a code system in one of the other files
        # for that disease. This allows us to simply append the contents of `compose.include` into that
        # element in `out`.
        with open(os.path.join(root, source_path)) as f:
            source = json.load(f)
        out['compose']['include'] += source['compose']['include']

    # Write output
    with open(os.path.join(root, 'input', 'vocabulary', f'immunization-{disease.lower()}-all.json'), 'w') as f:
        f.write(json.dumps(out, indent=2))
