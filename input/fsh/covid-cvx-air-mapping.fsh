Instance: covid-cvx-air-mapping
InstanceOf: ConceptMap
Title: "Mapping between CVX and AIR Covid Codes"
Description: "A Mapping between CVX and AIR Codes for Covid vaccinations. This mapping is bi-directional - one group for each direction"
Usage: #definition
* url = "https://github.com/dvci/shc-terminology/ConceptMap/covid-cvx-air-mapping"
* version = "4.0.1"
* name = "CovidCVXandAIRCodeMapping"
* title = "Mapping between CVX and AIR Covid Codes"
* status = #draft
* date = "2021-09-22"
* publisher = "Health Intersections"
* contact.name = "Grahame Grieve"
* contact.telecom.system = #email
* contact.telecom.value = "grahame@healthintersections.com.au"
* description = "A Mapping between CVX and AIR Codes for Covid vaccinations. This mapping is bi-directional - one group for each direction"
* jurisdiction = urn:iso:std:iso:3166#AU
* copyright = "Creative Commons 0"
* group[0].source = "https://www.humanservices.gov.au/organisations/health-professionals/enablers/air-vaccine-code-formats"
* group[=].sourceVersion = "20210222"
* group[=].target = "http://hl7.org/fhir/sid/cvx"
* group[=].element[0].code = #COVAST
* group[=].element[=].display = "COVID-19 Vaccine AstraZeneca"
* group[=].element[=].target.code = #210
* group[=].element[=].target.display = "COVID-19 vaccine, vector-nr, rS-ChAdOx1, PF, 0.5 mL"
* group[=].element[=].target.equivalence = #equivalent
* group[=].element[+].code = #COMIRN
* group[=].element[=].display = "Pfizer Comirnaty"
* group[=].element[=].target.code = #208
* group[=].element[=].target.display = "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose"
* group[=].element[=].target.equivalence = #equivalent
* group[=].element[+].code = #MODERN
* group[=].element[=].display = "Moderna Spikevax"
* group[=].element[=].target.code = #207
* group[=].element[=].target.display = "COVID-19, mRNA, LNP-S, PF, 100 mcg or 50 mcg dose"
* group[=].element[=].target.equivalence = #equivalent
* group[+].source = "http://hl7.org/fhir/sid/cvx"
* group[=].target = "https://www.humanservices.gov.au/organisations/health-professionals/enablers/air-vaccine-code-formats"
* group[=].targetVersion = "20210222"
* group[=].element[0].code = #210
* group[=].element[=].display = "COVID-19 vaccine, vector-nr, rS-ChAdOx1, PF, 0.5 mL"
* group[=].element[=].target.code = #COVAST
* group[=].element[=].target.display = "COVID-19 Vaccine AstraZeneca"
* group[=].element[=].target.equivalence = #equivalent
* group[=].element[+].code = #208
* group[=].element[=].display = "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose"
* group[=].element[=].target.code = #COMIRN
* group[=].element[=].target.display = "Pfizer Comirnaty"
* group[=].element[=].target.equivalence = #equivalent
* group[=].element[+].code = #207
* group[=].element[=].display = "COVID-19, mRNA, LNP-S, PF, 100 mcg or 50 mcg dose"
* group[=].element[=].target.code = #MODERN
* group[=].element[=].target.display = "Moderna Spikevax"
* group[=].element[=].target.equivalence = #equivalent
* group[=].element[+].code = #211
* group[=].element[=].display = "COVID-19 vaccine, Subunit, rS-nanoparticle+Matrix-M1 Adjuvant, PF, 0.5 mL"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #212
* group[=].element[=].display = "COVID-19 vaccine, vector-nr, rS-Ad26, PF, 0.5 mL"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #213
* group[=].element[=].display = "SARS-COV-2 (COVID-19) vaccine, UNSPECIFIED"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #217
* group[=].element[=].display = "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose, tris-sucrose"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #218
* group[=].element[=].display = "COVID-19, mRNA, LNP-S, PF, 10 mcg/0.2 mL dose, tris-sucrose"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #219
* group[=].element[=].display = "COVID-19, mRNA, LNP-S, PF, 3 mcg/0.2 mL dose, tris-sucrose"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #500
* group[=].element[=].display = "COVID-19 Non-US Vaccine, Product Unknown"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #501
* group[=].element[=].display = "COVID-19 IV Non-US Vaccine (QAZCOVID-IN)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #502
* group[=].element[=].display = "COVID-19 IV Non-US Vaccine (COVAXIN)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #503
* group[=].element[=].display = "COVID-19 LAV Non-US Vaccine (COVIVAC)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #504
* group[=].element[=].display = "COVID-19 VVnr Non-US Vaccine (Sputnik Light)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #505
* group[=].element[=].display = "COVID-19 VVnr Non-US Vaccine (Sputnik V)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #506
* group[=].element[=].display = "COVID-19 VVnr Non-US Vaccine (CanSino Biological Inc./Beijing Institute of Biotechnology)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #507
* group[=].element[=].display = "COVID-19 PS Non-US Vaccine (Anhui Zhifei Longcom Biopharm + Inst of Micro, Chinese Acad of Sciences)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #508
* group[=].element[=].display = "COVID-19 PS Non-US Vaccine (Jiangsu Province Centers for Disease Control and Prevention)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #509
* group[=].element[=].display = "COVID-19 PS Non-US Vaccine (EpiVacCorona)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #510
* group[=].element[=].display = "COVID-19 IV Non-US Vaccine (BIBP, Sinopharm)"
* group[=].element[=].target.equivalence = #unmatched
* group[=].element[+].code = #511
* group[=].element[=].display = "COVID-19 IV Non-US Vaccine (CoronaVac, Sinovac)"
* group[=].element[=].target.equivalence = #unmatched