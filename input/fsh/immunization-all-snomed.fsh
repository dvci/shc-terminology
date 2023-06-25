Alias: $snomed = http://snomed.info/sct

ValueSet: ImmunizationAllSnomedValueSet
Id: immunization-all-snomed
Title: "Immunization / All / SNOMED CT"
Description: "Contains descendants of SNOMED CT concept `787859002` \"Vaccine product (medicinal product)\". Note that codes from _any_ SNOMED CT extension are valid as long as they descend from this concept."

* ^copyright = "© 2002+ International Health Terminology Standards Development Organisation (IHTSDO)"

* include codes from system $snomed where concept descendent-of #787859002