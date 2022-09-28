### Source data

This value set contains all [CVX codes as published by CDC](https://www2.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx) related to monkeypox.

### Updating this value set

The CVX codes from CDC are curated into a JSON file on GitHub:

<a href="https://github.com/dvci/shc-terminology/blob/main/input/vocabulary/orthopoxvirus-cvx.json" class="btn btn-primary btn-lg">Edit on GitHub</a>

A [helper script](https://github.com/dvci/shc-terminology/blob/main/script/cvx/) can be run to automatically add newly published CVX codes. This script will preserve manually defined [`consumer-friendly`](https://terminology.smarthealth.cards/CodeSystem-designation-use.html) display text in this JSON file.

If you manually edit this JSON file, please run [`prettier`](https://prettier.io/) to ensure your JSON is valid and the formatting stays consistent. Please see the [README on GitHub](https://github.com/dvci/shc-terminology/blob/main/README.md) for more information.