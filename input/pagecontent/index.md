This website is a community-maintained terminology resource for implementers of [SMART Health Cards](https://smarthealth.cards/).

It provides both human-readable terminology resources, as well as computable versions in the form of [JSON](https://www.json.org) representations of [FHIR Resources](https://www.hl7.org/fhir/resource.html).

### Terminology for All Health Cards

#### Credential Types

SMART Health Cards are identified by one or more [credential types described in this CodeSystem](CodeSystem-health-card.html) (see the [SMART Health Cards specification](https://spec.smarthealth.cards/#health-cards-are-encoded-as-compact-serialization-json-web-signatures-jws) for more information). Each combination of credential types may be associated with a FHIR Implementation Guide and/or type-specific terminology. This site provides support for the latter.

#### Identity Assurance Level

The codes in [this CodeSystem](CodeSystem-identity-assurance-level.html) may be used by Issuers of SMART Health Cards to record if/how a patient's identity was verified at the point of care. For example, if a patient showed their driver's license to verify their name and date of birth when getting a vaccination, this would correspond to `IAL1.4`.

### Terminology by FHIR Implementation Guide (IG)

#### Vaccination & Testing IG

The [SMART Health Cards: Vaccination & Testing Implementation Guide](https://vci.org/ig/vaccination-and-testing) describes the patient information and clinical data contained in [`#immunization`](CodeSystem-health-card.html) and [`#laboratory`](CodeSystem-health-card.html)-type SMART Health Cards related to infectious diseases.

{% include credential_types.html %}

### Terminology Versioning

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
/* Hide toc */
.markdown-toc {
  display: none;
}
</style>