The following FHIR resources are provided as a community resource for implementers of [SMART Health Cards](https://smarthealth.cards/).

### Vaccines

SMART Health Cards for vaccines typically use either [CVX](https://www2.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx) or [SNOMED CT](https://www.snomed.org/) to identify the administered vaccine, and occasionally [ICD-11](https://icdcdn.who.int/icd11referenceguide/en/html/index.html) may also be used. For more details please see [the SMART Health Cards Vaccination Profile](https://vci.org/ig/vaccination-and-testing/StructureDefinition-shc-vaccination-dm.html).

The following ValueSets are provided to assist implementers wishing to identify vaccines for specific diseases:

* **COVID-19**
  * [CVX](ValueSet-covid-cvx.html)
  * ICD-11 (forthcoming)
  * [SNOMED CT](ValueSet-covid-19-vaccine-snomed-value-set.html)
* **Monkeypox**
  * [CVX](ValueSet-monkeypox-cvx.html)
  * ICD-11 (forthcoming)
  * SNOMED CT (forthcoming)

### Infectious disease-related laboratory testing

SMART Health Cards use [LOINC](https://loinc.org/) to identify laboratory tests related to infectious diseases (including COVID-19).

Lab test results are identified using [SNOMED CT](https://www.snomed.org/) whenever possible, with [LOINC Answer codes](https://loinc.org/answer-file/) as a fallback.

The following ValueSets are provided to assist implementers of SMART Health Cards representing infectious disease-related laboratory tests and test results:

* [LOINCs for COVID-19-related qualitative laboratory tests](ValueSet-qualitative-covid-lab-test-value-set.html)
* [SNOMED CT codes and LOINC Answer codes for qualitative laboratory tests](ValueSet-qualitative-lab-test-result-value-set.html), including for COVID-19 and other infectious diseases

### SMART Health Card Types

The [health card type code system](CodeSystem-health-card.html) contains the codes used to identify the credential type. See the [SMART Health Cards specification](https://spec.smarthealth.cards/#health-cards-are-encoded-as-compact-serialization-json-web-signatures-jws) for more information.

### Identity Assurance Level

[These codes](CodeSystem-identity-assurance-level.html) may be used by Issuers of SMART Health Cards to record if/how a patient's identity was verified at the point of care. For example, if a patient showed their driver's license to verify their name and date of birth when getting a vaccination, this would correspond to `IAL1.4`.

### Designation Use

[The `consumer-friendly` code in this code system](CodeSystem-designation-use.html) is used in a [ValueSet's designation element](https://www.hl7.org/fhir/valueset-definitions.html#ValueSet.compose.include.concept.designation) to define how that designation should be used. 

----

### Contact Information

For technical questions, please post on the [smart/health-cards Zulip stream at chat.fhir.org](https://chat.fhir.org/#narrow/stream/284830-smart.2Fhealth-cards) (a free account is required).

This website is maintained by [VCI](https://vci.org).

### Contributing

The source code for this website and the FHIR resources contained within are available on GitHub, and community contributions are welcome. Please see <https://github.com/dvci/shc-terminology/> for details.