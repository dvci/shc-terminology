# ICD-11 MMS Scripts

Ths folder contains Python scripts used to retrieve data from the [ICD API].

Accessing this API requires registering for a (free) account. Set the `ICD11_CLIENT` and `ICD11_CLIENT_SECRET` environment variables to the values of [ClientId and ClientSecret from the ICD API](https://icd.who.int/icdapi/Account/AccessKey) respectively.

- `icd11.py` provides a Python class (`Icd11Fetcher`) to access this API.
- `icd11_test.py` has some unit tests for `Icd11Fetcher`.
- `get_all_vaccine_descendants.py` prints out all the ICD-11 MMS codes that descend from the WHO-FIC Foundation "Vaccines" entity (`http://id.who.int/icd/entity/164949870`)
- `get_covid19_vaccine_descendants_fsh.py` prints out the contents of `input/fsh/immunization-covid-icd11.fsh` using the latest data from the ICD-11 API.

Note that there is no ICD-11 MMS code that corresponds to `http://id.who.int/icd/entity/164949870` ("Vaccines") in the WHO-FIC Foundation.

[ICD API]: https://icd.who.int/icdapi
