This website is a community-maintained terminology resource for implementers of [SMART Health Cards](https://smarthealth.cards/).

It provides both human-readable terminology resources, as well as computable versions in the form of [JSON](https://www.json.org) representations of [FHIR Resources](https://www.hl7.org/fhir/resource.html).

### Use Case-Specific Terminology

FHIR Implementation Guides (IGs) are used to specify the FHIR payload within SMART Health Cards.

#### Vaccination & Testing IG

The [SMART Health Cards: Vaccination & Testing Implementation Guide](https://vci.org/ig/vaccination-and-testing) describes the patient information and clinical data contained in SMART Health Cards related to vaccinations and qualitative laboratory testing for infectious diseases. Terminology relevant to these use cases is described in the table below.

{% include credential_types.html %}

### Terminology for All SMART Health Cards

#### Identity Assurance Level

The codes in [this CodeSystem](CodeSystem-identity-assurance-level.html) may be used by Issuers of SMART Health Cards to record if/how a patient's identity was verified at the point of care. For example, if a patient showed their driver's license to verify their name and date of birth when getting a vaccination, this would correspond to `IAL1.4`.

#### `#health-card`

SMART Health Cards are identified by a `vc.type` value of `https://smarthealth.cards#health-card`, which is defined [in this CodeSystem](CodeSystem-health-card.html). See the [SMART Health Cards specification](https://spec.smarthealth.cards/#health-cards-are-encoded-as-compact-serialization-json-web-signatures-jws) for more information.

### Terminology Versioning

ValueSets from medical terminology (e.g., CVX, LOINC, etc.) are versioned using a `YYYY.n` format where `YYYY` is the year a given version was created and `n` is an incremented integer.

Unified terminology ValueSets (e.g., [all COVID-19 vaccine codes](ValueSet-immunization-covid-all.html)) are versioned with the date they were generated (e.g., `20230101` for generation on Jan 1, 2023).

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
/* Hide toc */
.markdown-toc {
  display: none;
}
</style>
