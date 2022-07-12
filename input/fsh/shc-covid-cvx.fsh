// Instance: shc-covid-cvx
// InstanceOf: ValueSet
// Title: "CVX Covid Codes for use in Smart Health Cards"
// Description: "A list of CVX codes with recommended consumer suitable displays for use in Smart Health Cards, with localized consumer friendly terms"
// Usage: #definition
// * include codes from system DesignationUseCaseCodeSystem
// * language = #en
// * url = "https://github.com/dvci/shc-terminology/ValueSet/shc-covid-cvx"
// * version = "4.0.1"
// * name = "ShcCovidCvxCodes"
// * title = "CVX Covid Codes for use in Smart Health Cards"
// * status = #draft
// * date = "2021-09-22"
// * publisher = "Health Intersections"
// * contact.name = "Grahame Grieve"
// * contact.telecom.system = #email
// * contact.telecom.value = "grahame@healthintersections.com.au"
// * description = "A list of CVX codes with recommended consumer suitable displays for use in Smart Health Cards, with localized consumer friendly terms"
// * jurisdiction = urn:iso:std:iso:3166#AU
// * copyright = "Creative Commons 0"
// * compose.include.system = "http://hl7.org/fhir/sid/cvx"
// * compose.include.concept[0].code = #210
// * compose.include.concept[=].display = "COVID-19 vaccine, vector-nr, rS-ChAdOx1, PF, 0.5 mL"
// * compose.include.concept[=].designation[0].language = #en-AU
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "AstraZeneca (Vaxzevria)"
// * compose.include.concept[=].designation[+].language = #en-US
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "AstraZeneca COVID-19 Vaccine"
// * compose.include.concept[+].code = #208
// * compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose"
// * compose.include.concept[=].designation[0].language = #en-AU
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Pfizer (Comirnaty)"
// * compose.include.concept[=].designation[+].language = #en-US
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
// * compose.include.concept[=].designation[+].language = #en-NZ
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
// * compose.include.concept[+].code = #207
// * compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 100 mcg or 50 mcg dose"
// * compose.include.concept[=].designation[0].language = #en-AU
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Moderna (Spikevax)"
// * compose.include.concept[=].designation[+].language = #en-US
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Moderna COVID-19 Vaccine"
// * compose.include.concept[+].code = #212
// * compose.include.concept[=].display = "COVID-19 vaccine, vector-nr, rS-Ad26, PF, 0.5 mL"
// * compose.include.concept[=].designation[0].language = #en-AU
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Janssen COVID-19 Vaccine"
// * compose.include.concept[=].designation[+].language = #en-US
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Janssen COVID-19 Vaccine"
// * compose.include.concept[+].code = #217
// * compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose, tris-sucrose"
// * compose.include.concept[=].designation[0].language = #en-AU
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Pfizer (Comirnaty)"
// * compose.include.concept[=].designation[+].language = #en-US
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
// * compose.include.concept[+].code = #218
// * compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 10 mcg/0.2 mL dose, tris-sucrose"
// * compose.include.concept[=].designation[0].language = #en-AU
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Pfizer (Comirnaty) - Child dose"
// * compose.include.concept[=].designation[+].language = #en-US
// * compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation[=].use.use = "consumer-friendly"
// * compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
// * compose.include.concept[+].code = #510
// * compose.include.concept[=].display = "COVID-19 IV Non-US Vaccine (BIBP, Sinopharm)"
// * compose.include.concept[=].designation.language = #en-US
// * compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation.use.use = "consumer-friendly"
// * compose.include.concept[=].designation.value = "Sinopharm (BIBP) COVID-19 Vaccine"
// * compose.include.concept[+].code = #511
// * compose.include.concept[=].display = "COVID-19 IV Non-US Vaccine (CoronaVac, Sinovac)"
// * compose.include.concept[=].designation.language = #en-US
// * compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation.use.use = "consumer-friendly"
// * compose.include.concept[=].designation.value = "Coronavac (Sinovac) COVID-19 Vaccine"
// * compose.include.concept[+].code = #211
// * compose.include.concept[=].display = "COVID-19 vaccine, Subunit, rS-nanoparticle+Matrix-M1 Adjuvant, PF, 0.5 mL"
// * compose.include.concept[=].designation.language = #en-US
// * compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation.use.use = "consumer-friendly"
// * compose.include.concept[=].designation.value = "Novavax COVID-19 Vaccine"
// * compose.include.concept[+].code = #219
// * compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 3 mcg/0.2 mL dose, tris-sucrose"
// * compose.include.concept[=].designation.language = #en-US
// * compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation.use.use = "consumer-friendly"
// * compose.include.concept[=].designation.value = "Pfizer-BioNTech COVID-19 Vaccine (EUA labeled) COMIRNATY (BLA labeled)"
// * compose.include.concept[+].code = #502
// * compose.include.concept[=].display = "COVID-19 IV Non-US Vaccine (COVAXIN)"
// * compose.include.concept[=].designation.language = #en-US
// * compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
// * compose.include.concept[=].designation.use.use = "consumer-friendly"
// * compose.include.concept[=].designation.value = "COVAXIN (Bharat) COVID-19 Vaccine"


ValueSet: ShcCovidCvx
Id: shc-covid-cvx
Title: "CVX Covid Codes for use in Smart Health Cards"
Description: "A list of CVX codes with recommended consumer suitable displays for use in Smart Health Cards, with localized consumer friendly terms"
* include codes from system DesignationUseCaseCodeSystem
// * language = #en
* ^url = "https://github.com/dvci/shc-terminology/ValueSet/shc-covid-cvx"
* ^version = "4.0.1"
* ^name = "ShcCovidCvxCodes"
* ^title = "CVX Covid Codes for use in Smart Health Cards"
* ^status = #draft
* ^date = "2021-09-22"
* ^publisher = "Health Intersections"
* ^contact.name = "Grahame Grieve"
* ^contact.telecom.system = #email
* ^contact.telecom.value = "grahame@healthintersections.com.au"
* ^description = "A list of CVX codes with recommended consumer suitable displays for use in Smart Health Cards, with localized consumer friendly terms"
* ^jurisdiction = urn:iso:std:iso:3166#AU
* ^copyright = "Creative Commons 0"
* ^compose.include.system = "http://hl7.org/fhir/sid/cvx"
* ^compose.include.concept[0].code = #210
* ^compose.include.concept[=].display = "COVID-19 vaccine, vector-nr, rS-ChAdOx1, PF, 0.5 mL"
* ^compose.include.concept[=].designation[0].language = #en-AU
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "AstraZeneca (Vaxzevria)"
* ^compose.include.concept[=].designation[+].language = #en-US
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "AstraZeneca COVID-19 Vaccine"
* ^compose.include.concept[+].code = #208
* ^compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose"
* ^compose.include.concept[=].designation[0].language = #en-AU
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Pfizer (Comirnaty)"
* ^compose.include.concept[=].designation[+].language = #en-US
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
* ^compose.include.concept[=].designation[+].language = #en-NZ
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
* ^compose.include.concept[+].code = #207
* ^compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 100 mcg or 50 mcg dose"
* ^compose.include.concept[=].designation[0].language = #en-AU
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Moderna (Spikevax)"
* ^compose.include.concept[=].designation[+].language = #en-US
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Moderna COVID-19 Vaccine"
* ^compose.include.concept[+].code = #212
* ^compose.include.concept[=].display = "COVID-19 vaccine, vector-nr, rS-Ad26, PF, 0.5 mL"
* ^compose.include.concept[=].designation[0].language = #en-AU
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Janssen COVID-19 Vaccine"
* ^compose.include.concept[=].designation[+].language = #en-US
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Janssen COVID-19 Vaccine"
* ^compose.include.concept[+].code = #217
* ^compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose, tris-sucrose"
* ^compose.include.concept[=].designation[0].language = #en-AU
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Pfizer (Comirnaty)"
* ^compose.include.concept[=].designation[+].language = #en-US
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
* ^compose.include.concept[+].code = #218
* ^compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 10 mcg/0.2 mL dose, tris-sucrose"
* ^compose.include.concept[=].designation[0].language = #en-AU
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Pfizer (Comirnaty) - Child dose"
* ^compose.include.concept[=].designation[+].language = #en-US
* ^compose.include.concept[=].designation[=].use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation[=].use.display = "consumer-friendly"
* ^compose.include.concept[=].designation[=].value = "Pfizer-BioNTech COVID-19 Vaccine"
* ^compose.include.concept[+].code = #510
* ^compose.include.concept[=].display = "COVID-19 IV Non-US Vaccine (BIBP, Sinopharm)"
* ^compose.include.concept[=].designation.language = #en-US
* ^compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation.use.display = "consumer-friendly"
* ^compose.include.concept[=].designation.value = "Sinopharm (BIBP) COVID-19 Vaccine"
* ^compose.include.concept[+].code = #511
* ^compose.include.concept[=].display = "COVID-19 IV Non-US Vaccine (CoronaVac, Sinovac)"
* ^compose.include.concept[=].designation.language = #en-US
* ^compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation.use.display = "consumer-friendly"
* ^compose.include.concept[=].designation.value = "Coronavac (Sinovac) COVID-19 Vaccine"
* ^compose.include.concept[+].code = #211
* ^compose.include.concept[=].display = "COVID-19 vaccine, Subunit, rS-nanoparticle+Matrix-M1 Adjuvant, PF, 0.5 mL"
* ^compose.include.concept[=].designation.language = #en-US
* ^compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation.use.display = "consumer-friendly"
* ^compose.include.concept[=].designation.value = "Novavax COVID-19 Vaccine"
* ^compose.include.concept[+].code = #219
* ^compose.include.concept[=].display = "COVID-19, mRNA, LNP-S, PF, 3 mcg/0.2 mL dose, tris-sucrose"
* ^compose.include.concept[=].designation.language = #en-US
* ^compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation.use.display = "consumer-friendly"
* ^compose.include.concept[=].designation.value = "Pfizer-BioNTech COVID-19 Vaccine (EUA labeled) COMIRNATY (BLA labeled)"
* ^compose.include.concept[+].code = #502
* ^compose.include.concept[=].display = "COVID-19 IV Non-US Vaccine (COVAXIN)"
* ^compose.include.concept[=].designation.language = #en-US
* ^compose.include.concept[=].designation.use.system = "http://example.org/fhir/CodeSystem/designation-use"
* ^compose.include.concept[=].designation.use.display = "consumer-friendly"
* ^compose.include.concept[=].designation.value = "COVAXIN (Bharat) COVID-19 Vaccine"

// CodeSystem: DesignationUseCaseCodeSystem
// Id: designation-use-case-code-system
// Title: "Designation Use Case"
// Description: "Use Case for the vaccination designation"
// * #consumer-friendly "Consumer-friendly"