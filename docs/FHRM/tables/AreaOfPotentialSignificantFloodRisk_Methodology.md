# AreaOfPotentialSignificantFloodRisk_Methodology

## Description

APSFR: Area of Potential Significant Flood Risk - Methodology
This dataset provides information on the overall approach, methodology, and criteria used for designating APSFRs, as well as, where relevant, details on national and international coordination mechanisms in place.
Uniqueness: euFloodsUnitOfManagementCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0201
  - The euFloodsUnitOfManagementCode must be unique.
* - XC0298
  - The table AreaOfPotentialSignificantFloodRisk\_Methodology does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0301
  - The table AreaOfPotentialSignificantFloodRisk\_Methodology contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
```

### euFloodsUnitOfManagementCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 42 characters. Required. Unique EU code for the Unit of Management or WFD River Basin District following the WISE identifier syntax. Add the two-letter ISO Country code to the Member State unique id - up to 42 characters in total.
* - Field type
  - FeatureUniqueEUCodeType
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0229
  - The length must be less than or equal to 42
* - V0230
  - The value does not match the pattern to be used
* - V0253
  - The value must not be missing or empty
* - XC0296
  - euFloodsUnitOfManagementCode must exist on table dcMetadata
```

### url

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. URL for integration of your own internet-based information that provides access to further relevant details on the nature and characteristics of the APSFR that will help in the interpretation of flood risk and flood risk management.
* - Field type
  - URL
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0209
  - The value does not follow the expected syntax for a valid URL
* - V0289
  - The length must be less than or equal to 2100
```

### internationalUOM

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose an option from the 'YesNo' codelist values. Is the UoM international? If ‘Yes’, please provide the information requested in the schema elements below, relating to mechanisms of coordination.
* - Field type
  - YesNo
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - RF0201
  - internationalUOM field needs to match with referenceData relatedZones/international value.
* - V0231
  - The value does not exist in codelist YesNo
* - V0270
  - The value must not be missing or empty
```

### overallApproachReviewReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide a reference or references describing how the review process to the overall approach and methodology applied to designate APSFRs has been undertaken and, where relavant, what changes have been implemented since the previous cycle of reporting. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - DocumentReference
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0269
  - The value must not be missing or empty
* - V0273
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0202
  - The document reference does not exist
```

### criteriaDeterminationUsed

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'CriteriaForDeterminationFloodRisk' codelist values. Provide the criteria used for determination of areas as APSFRs. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - CriteriaForDeterminationFloodRisk
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0232
  - The value does not exist in codelist CriteriaForDeterminationFloodRisk
* - V0267
  - The value must not be missing or empty
* - V0274
  - Duplicate values for criteriaDeterminationUsed exist. The list of values needs to be distinct in each record.
```

### criteriaDeterminationExpertJudgementDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Expert Judgement’ has been selected from enumeration list, provide a brief description as to how expert judgement was used to determine significant flood risk.
* - Field type
  - String
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R0203
  - criteriaDeterminationExpertJudgementDescription must be reported if criteriaDeterminationUsed is 'expertJudgement'
* - V0288
  - The length must be less than or equal to 1000
```

### otherCriteriaDetermination

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ selected from enumeration list. Provide a description of what other criteria have been used to determine significant flood risk.
* - Field type
  - String
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R0204
  - otherCriteriaDetermination must be reported if criteriaDeterminationUsed contains 'other' as an option
* - V0233
  - The length must be less than or equal to 1000
```

### criteriaDeterminationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) detailing the overall methodology used to determine flood risk. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - DocumentReference
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0266
  - The value must not be missing or empty
* - V0275
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0203
  - The document reference does not exist
```

### criteriaInclusionUsed

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide the criteria used for inclusion of significant flood risk from the 'CriteriaForInclusion' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - CriteriaForInclusion
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0234
  - The value does not exist in codelist CriteriaForInclusion
* - V0268
  - The value must not be missing or empty
* - V0276
  - Duplicate values for criteriaInclusionUsed exist. The list of values needs to be distinct in each record.
```

### otherCriteriaInclusion

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ selected from enumeration list. Provide a description of what other criteria has been used to determine inclusion of areas as APSFRs.
* - Field type
  - String
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R0205
  - otherCriteriaInclusion must be reported if criteriaInclusionUsed is 'other'
* - V0235
  - The length must be less than or equal to 1000
```

### considerationsConsequencesHumanHealth

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose an option from the 'YesNo' codelist values. Please indicate whether specific criteria relating to human health have been used in the identification of APSFRs.
* - Field type
  - YesNo
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0236
  - The value does not exist in codelist YesNo
* - V0264
  - The value must not be missing or empty
```

### considerationsConsequencesEnvironment

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose an option from the 'YesNo' codelist values. Please indicate whether specific criteria relating to environment have been used in the identification of APSFRs.
* - Field type
  - YesNo
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0237
  - The value does not exist in codelist YesNo
* - V0263
  - The value must not be missing or empty
```

### considerationsConsequencesCulturalHeritage

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose an option from the 'YesNo' codelist values. Please indicate whether specific criteria relating to cultural heritage have been used in the identification of APSFRs.
* - Field type
  - YesNo
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0238
  - The value does not exist in codelist YesNo
* - V0261
  - The value must not be missing or empty
```

### considerationsConsequencesEconomicActivity

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose an option from the 'YesNo' codelist values. Please indicate whether specific criteria relating to economic activity have been used in the identification of APSFRs.
* - Field type
  - YesNo
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0239
  - The value does not exist in codelist YesNo
* - V0262
  - The value must not be missing or empty
```

### considerationsConsequencesMethodologyReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. If 'yes' to 'ConsiderationOfConsequences' for any of the elements above (Human Health, Environment, Cultural Heritage or Economic Activity), provide document(s) or link(s) detailing the overall methodology used to determine flood risk with respect to the definition of an APSFR; if 'no', provide reasons for not including any of these elements (this can include a link to a reference document(s) or simply a link to reference in the form of a summary document. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - DocumentReference
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0265
  - The value must not be missing or empty
* - V0277
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0204
  - The document reference does not exist
```

### mechanismsInternationalCoordUsed

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Choose from the 'InternationalInformationExchange' codelist values. Only for international UoMs/RBDs which have international APSFRs. What mechanisms of coordination have taken place between MS and countries within international RBDs or International units of management? More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - InternationalInformationExchange
* - minOccurs
  - 0
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R0213
  - If internationalUOM = 'Yes', mechanismsInternationalCoordUsed must be reported
* - V0240
  - The value does not exist in codelist InternationalInformationExchange
* - V0278
  - Duplicate values for mechanismsInternationalCoordUsed exist. The list of values needs to be distinct in each record.
* - V0291
  - The option 'none' is not compatible with any other option.
```

### otherMechanismsInternationalCoord

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ selected from enumeration list. Provide a description of what other mechanisms have been used for coordination.
* - Field type
  - String
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R0206
  - otherMechanismsInternationalCoord must be reported if mechanismsInternationalCoordUsed is 'other'
* - V0241
  - The length must be less than or equal to 1000
```

### mechanismsInternationalCoordReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required, only for international UoMs/RBDs. Provide document(s) or link(s) detailing the coordination mechanisms that are in place. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - DocumentReference
* - minOccurs
  - 0
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0279
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0205
  - The document reference does not exist
```

### noInformationExchangeExplanation

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘none’ is selected from enumeration list. Provide an explanation as to why this was the case.
* - Field type
  - String
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R0207
  - noInformationExchangeExplanation must be reported if mechanismsInternationalCoordUsed is 'none'
* - V0242
  - The length must be less than or equal to 1000
```
