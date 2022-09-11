This website is a community-maintained terminology resource for implementers of [SMART Health Cards](https://smarthealth.cards/).

It provides both human-readable terminology resources, as well as computable versions in the form of [JSON](https://www.json.org) representations of [FHIR Resources](https://www.hl7.org/fhir/resource.html).

### Vaccines

Typically, SMART Health Cards for vaccines use either [CVX](https://www2.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx) or [SNOMED CT](https://www.snomed.org/) to identify the administered vaccine. [ICD-11](https://icdcdn.who.int/icd11referenceguide/en/html/index.html) may also be used. For more details please see [the SMART Health Cards Vaccination Profile](https://vci.org/ig/vaccination-and-testing/StructureDefinition-shc-vaccination-dm.html) for more information.

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

----

### Versioning

ValueSets from medical terminology (e.g., CVX, LOINC, etc.) are versioned using a `YYYY.n` format where `YYYY` is the year a given version was created and `n` is an incremented integer.

Other terminology resources are versioned with [semantic versioning](https://semver.org/).

(Semantic versioning is not used for the medical terminology ValueSets because that there is no notion of "incompatible" changes, meaning that the first semantic versioning digit representing the "major" version would _never_ be incremented. This would eventually lead to version numbers like `1.1234.0`.)

### Contact Information

For technical questions, please post on the [smart/health-cards Zulip stream at chat.fhir.org](https://chat.fhir.org/#narrow/stream/284830-smart.2Fhealth-cards) (free account required).

This website is maintained for the SMART Health Card implementer community by [VCI](https://vci.org).

### Contributing

The source code for this website and the FHIR resources contained within are available on GitHub, and community contributions are welcome. Please see <https://github.com/dvci/shc-terminology/> for details.

<style>
/* Hide metadata table at top of page */
.colsd {
  display: none;
}
</style>