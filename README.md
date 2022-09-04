# SMART Health Card Terminology

This is the source code for <https://terminology.smarthealth.cards>.

## Localization

"Consumer friendly" display text localizations may be added to the ValueSet resources in this repository. For example, see the [COVID CVX value set](https://github.com/dvci/shc-terminology/blob/main/input/vocabulary/covid-cvx.json), which includes localization like the following example under the `designation` element:

```json
{
  "code": "207",
  "display": "COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose",
  "designation": [
    {
      "language": "en-AU",
      "use": {
        "system": "https://terminology.smarthealth.cards/CodeSystem/designation-use",
        "use": "consumer-friendly"
      },
      "value": "Moderna (Spikevax)"
    },
    {
      "language": "en-US",
      "use": {
        "system": "https://terminology.smarthealth.cards/CodeSystem/designation-use",
        "use": "consumer-friendly"
      },
      "value": "Moderna COVID-19 Vaccine"
    }
  ]
}
```

Localizations are scoped using `designation.language`, which is a [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag). The FHIR spec provides a [list of common BCP 47 language tags](https://www.hl7.org/fhir/valueset-languages.html), but any BCP 47 tag may be used. Use the broadest applicable tag for a given localization.

Ideally localizations will be based on authoritative sources, e.g., documentation from a jurisdiction's government agency that approves pharmaceuticals for use. However, localizations in this repository are community-provided, and therefore may not be correct. If you notice a problem, please fix it in a pull request or use the chat.fhir.org link below to notify the community. If you contribute a localization, please document the source/justification for localization additions or changes in the commit message ([example](https://github.com/dvci/shc-terminology/commit/91d7ee11467da7c50fda89711ab8d1e2499b10f4).

## Contributing

Pull requests are welcome.

For technical questions or comments, please post on the [smart/health-cards Zulip stream at chat.fhir.org](https://chat.fhir.org/#narrow/stream/284830-smart.2Fhealth-cards) (free account required).

### JSON formatting

We use [`prettier`](https://prettier.io) to format the contents of `input/vocabulary`. Please run `prettier --write input/vocabulary/*.json` before committing. (Formatting is checked on GitHub Pull Requests with CI.)

If you need to install `prettier`, you can run `npm install -g prettier` to install it system-wide.

----

## License

Copyright 2022 The MITRE Corporation

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
```
http://www.apache.org/licenses/LICENSE-2.0
```
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Code of Conduct

Everyone interacting in this project's codebases, issue trackers, chat rooms and mailing lists is expected to follow this [code of conduct](https://github.com/dvci/health_cards/blob/master/CODE_OF_CONDUCT.md).

----

MITRE: Approved for Public Release. Distribution Unlimited. Case Number 21-0225.