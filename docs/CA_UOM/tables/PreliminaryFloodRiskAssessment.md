# PreliminaryFloodRiskAssessment

## Description

Preliminary Flood Risk Assessment

Uniqueness: euFloodsUnitOfManagementCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - XC0431
  - The table PreliminaryFloodRiskAssessment does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0434
  - The table PreliminaryFloodRiskAssessment contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - TU0421
  - The euFloodsUnitOfManagementCode must be unique.
* - V0443
  - The length must be less than or equal to 42
* - V0444
  - The value does not match the pattern to be used
* - V0449
  - The value must not be missing or empty
```

### url

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. URL for integration of your own internet-based information.
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
* - V0451
  - The value does not follow the expected syntax for a valid URL
* - V0532
  - The length must be less than or equal to 2100
```

### article_2_1_SewageSystemsExcluded

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. State whether floods from sewage systems have been excluded as a source of flooding.
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
* - V0445
  - The value does not exist in codelist YesNo
* - V0454
  - The value must not be missing or empty
```

### article_4_2_a_MapsAvailable

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Map(s) according to Article 4.2(a) (to be coordinated with WFD reporting), including topography and land use.
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
* - V0446
  - The value does not exist in codelist YesNo
* - V0455
  - The value must not be missing or empty
```

### article_4_2_a_MapsDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. Provide a reason/description if 'Article4.2(a)Maps' is set to 'No'.
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
* - R0419
  - article\_4\_2\_a\_MapsDescription must be reported if article\_4\_2\_a\_MapsAvailable is 'no'
* - V0447
  - The length must be less than or equal to 1000
```

### article_4_2_a_MapsReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. Provide a reference(s) if 'Article4aMaps' is set to 'Yes'. Provide a reference(s) to the map(s) and to how the map(s) was (were) used in the preliminary flood risk assessment. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0420
  - article\_4\_2\_a\_MapsReference must be reported if article\_4\_2\_a\_MapsAvailable is 'yes'
* - V0505
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0400
  - The document reference does not exist
```

### article_4_2_b_PastAdverseConsequencesCriteriaUsed

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'HistoricalSignificantFloodsCriteria' codelist values. Criteria used to define past floods with significant adverse impacts, with likelihood of repetition. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - HistoricalSignificantFloodsCriteria
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
* - V0448
  - The value does not exist in codelist HistoricalSignificantFloodsCriteria
* - V0463
  - The value must not be missing or empty
* - V0506
  - Duplicate values for article\_4\_2\_b\_PastAdverseConsequencesCriteriaUsed exist. The list of values needs to be distinct in each record.
```

### article_4_2_b_PastAdverseConsequencesExpertJudgementDescript

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Optional.
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
* - R0400
  - article\_4\_2\_b\_PastAdverseConsequencesExpertJudgementDescript must be reported if article\_4\_2\_b\_PastAdverseConsequencesCriteriaUsed = 'expertJudgement'
* - V0400
  - The length must be less than or equal to 1000
```

### article_4_2_b_PastAdverseConsequencesCriteriaOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from enumeration list, provide a description of what other criteria (there may be several 'other' criteria) have been used to define past floods with significant adverse impacts, with likelihood of repetition.
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
* - R0401
  - article\_4\_2\_b\_PastAdverseConsequencesCriteriaOther must be reported if article\_4\_2\_b\_PastAdverseConsequencesCriteriaUsed = 'other'
* - V0401
  - The length must be less than or equal to 1000
```

### article_4_2_b_PastAdverseConsequencesReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) to the methodology and criteria used to identify and assess floods that occurred in the past and their past adverse consequences (including whether such consequences would be 'significant') and whether the likelihood of such floods remains relevant. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0456
  - The value must not be missing or empty
* - V0507
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0401
  - The document reference does not exist
```

### article_4_2_c_SignificantAdverseConsequencesCriteriaUsed

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'HistoricalSignificantFloodsCriteria' codelist values. Criteria used to define significant past floods (without known significant adverse impacts) with likelihood for significant adverse consequences in the future. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - HistoricalSignificantFloodsCriteria
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
* - V0402
  - The value does not exist in codelist HistoricalSignificantFloodsCriteria
* - V0464
  - The value must not be missing or empty
* - V0508
  - Duplicate values for article\_4\_2\_c\_SignificantAdverseConsequencesCriteriaUsed exist. The list of values needs to be distinct in each record.
```

### article_4_2_c_SignificantAdverseConsequencesExpertJudgementD

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. if 'Expert Judgement' has been selected from enumeration list, provide a brief description as to how expert judgement was used to define past floods (without known significant adverse impacts) with likelihood for significant adverse consequences in the future.
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
* - R0402
  - article\_4\_2\_c\_SignificantAdverseConsequencesExpertJudgementD must be reported if article\_4\_2\_c\_SignificantAdverseConsequencesCriteriaUsed = 'expertJudgement'
* - V0403
  - The length must be less than or equal to 1000
```

### article_4_2_c_SignificantAdverseConsequencesCriteriaOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from enumeration list, provide a description of what other criteria (there may be several 'other' criteria) have been used to define significant past floods (without known significant adverse impacts) with likelihood for significant adverse consequences in the future.
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
* - R0403
  - article\_4\_2\_c\_SignificantAdverseConsequencesCriteriaOther must be reported if article\_4\_2\_c\_SignificantAdverseConsequencesCriteriaUsed = 'other'
* - V0404
  - The length must be less than or equal to 1000
```

### article_4_2_c_SignificantAdverseConsequencesReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) to the methodology and criteria used to define significant past floods (without known significant adverse impacts) with likelihood for significant adverse consequences in the future. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0509
  - Duplicate document references exist. The list of values needs to be distinct.
* - V0547
  - The value must not be missing or empty
* - XC0402
  - The document reference does not exist
```

### article_4_2_d_Issues

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'IssuesArticle4\_2\_d' codelist values. Issues considered to support the assessment of potential adverse consequences of future floods. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - IssuesArticle4\_2\_d
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
* - V0405
  - The value does not exist in codelist IssuesArticle4\_2\_d
* - V0462
  - The value must not be missing or empty
* - V0510
  - Duplicate values for article\_4\_2\_d\_Issues exist. The list of values needs to be distinct in each record.
* - V0552
  - The option 'noAssessmentRequired' is not compatible with any other option.
```

### article_4_2_d_IssuesReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) to the information relating to how each of the issues identified under Article 4.2(d) were considered to support the assessment of potential adverse consequences of future floods including information on the methodologies applied to consider those issues. If the specific needs of the MS do not require an assessment under Article 4.2(d), please provide a reason. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0457
  - The value must not be missing or empty
* - V0511
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0403
  - The document reference does not exist
```

### article_4_2_d_PotentialAdverseConsequencesCriteriaUsed

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'PotentialAdverseConsequencesCriteria' codelist values. Criteria used to identify potential adverse consequences of future floods. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - PotentialAdverseConsequencesCriteria
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
* - V0406
  - The value does not exist in codelist PotentialAdverseConsequencesCriteria
* - V0465
  - The value must not be missing or empty
* - V0512
  - Duplicate values for article\_4\_2\_d\_PotentialAdverseConsequencesCriteriaUsed exist. The list of values needs to be distinct in each record.
* - V0554
  - The option 'noAssessmentRequired' is not compatible with any other option.
```

### article_4_2_d_PotentialAdverseConsequencesExpertJudgementDes

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Expert Judgement' is selected from enumeration list, provide a brief description as to how expert judgement was used to define potential adverse consequences of future floods.
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
* - R0404
  - article\_4\_2\_d\_PotentialAdverseConsequencesExpertJudgementDescrip must be reported if article\_4\_2\_d\_PotentialAdverseConsequencesCriteriaUsed = 'expertJudgement'
* - V0407
  - The length must be less than or equal to 1000
```

### article_4_2_d_PotentialAdverseConsequencesCriteriaOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from enumeration list, provide a description of what other criteria (there may be several 'other' criteria) have been used to define adverse consequences of future floods.
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
* - R0405
  - article\_4\_2\_d\_PotentialAdverseConsequencesCriteriaOther must be reported if article\_4\_2\_d\_PotentialAdverseConsequencesCriteriaUsed = 'other'
* - V0408
  - The length must be less than or equal to 1000
```

### article_4_2_d_PotentialAdverseConsequencesReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) to the methodology and criteria used to define significant past floods (without known significant adverse impacts) with likelihood for significant adverse consequences in the future. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0466
  - The value must not be missing or empty
* - V0513
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0404
  - The document reference does not exist
```

### article_4_3_InternationalInformationExchange

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'InternationalInformationExchange' codelist values. If UoM is international, identify mechanism(s) used for international exchange of information. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g.: "value1; value2; value3".
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
* - RF0401
  - article\_4\_3\_InternationalInformationExchange must be reported if UnitOfManagement.international from dataflow CA\_UOM is 'yes'
* - V0410
  - The value does not exist in codelist InternationalInformationExchange
* - V0514
  - Duplicate values for article\_4\_3\_InternationalInformationExchange exist. The list of values needs to be distinct in each record.
* - V0555
  - The option 'missing' is not compatible with any other option.
```

### article_4_3_InternationalInformationExchangeNoInformationExc

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'missing' is selected from enumeration list, provide an explanation as to why this was the case.
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
* - R0407
  - article\_4\_3\_InternationalInformationExchangeNoInformationExc must be reported if article\_4\_3\_InternationalInformationExchange contains 'missing' as an option
* - V0411
  - The length must be less than or equal to 1000
```

### article_4_3_InternationalInformationExchangeOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from enumeration list, provide a description of what other mechanisms of international information exchange have been used.
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
* - R0408
  - article\_4\_3\_InternationalInformationExchangeOther must be reported if article\_4\_3\_InternationalInformationExchange contains 'other' as an option
* - V0412
  - The length must be less than or equal to 1000
```

### article_4_3_InternationalInformationExchangeReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. If the UoM is international, provide document(s) or link(s) to document(s) relating to the information on the institutional relationships established to ensure coordination where a flood event covers the territory of more than one Member State or includes the territory of non-Member States. Include reference to international agreements, if they exist. Minutes from meetings that are publicly available could be referenced and reference to a report and/or summary would also be relevant. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - RF0402
  - article\_4\_3\_InternationalInformationExchangeReference must be reported if UnitOfManagement.international from dataflow CA\_UOM is 'yes'
* - V0515
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0405
  - The document reference does not exist
```

### article_14_1_OverallApproachReviewReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide a reference or references describing how the review process to the overall approach and methodology applied to undertake the PFRA has been undertaken and, where relevant, what changes have been implemented in the second cycle of reporting. An overview is required here not specific details relating to particular flood events or locations. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0450
  - The value must not be missing or empty
* - V0516
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0406
  - The document reference does not exist
```

### article_14_4_ConsiderationOfClimateChangeConsidered

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Has climate change been taken into consideration in the review of the PFRA?
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
* - V0413
  - The value does not exist in codelist YesNo
* - V0452
  - The value must not be missing or empty
```

### article_14_4_ConsiderationOfClimateChangeNotConsideredExplan

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'No' is selected from enumeration list, provide an explanation as to why this was the case.
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
* - R0410
  - article\_14\_4\_ConsiderationOfClimateChangeNotConsideredExplan must be if and only if article\_14\_4\_ConsiderationOfClimateChangeConsidered is 'no'
* - V0531
  - The length must be less than or equal to 1000
```

### article_14_4_ConsiderationOfClimateChangeReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. If 'Yes' is selected, provide document(s) or link(s) to the information relating to how climate change has been taken into consideration in the review of the PFRA. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0411
  - article\_14\_4\_ConsiderationOfClimateChangeReference must be reported article\_14\_4\_ConsiderationOfClimateChangeConsidered is 'yes'
* - V0517
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0407
  - The document reference does not exist
```

### informationCulturalHeritageReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) detailing methodologies used for assessing how the levels of past adverse impacts or potential adverse consequences on cultural heritage have been defined. References may include descriptions of approaches and available data used in the assessment. Note that generic approaches only are required (i.e. not related to specific flood events). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0458
  - The value must not be missing or empty
* - V0518
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0408
  - The document reference does not exist
```

### informationEconomicActivityReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) detailing methodologies used for assessing how the levels of past adverse impacts or potential adverse consequences on economic activity have been defined. References may include descriptions of approaches and available data used in the assessment. Note that generic approaches only are required (i.e. not related to specific flood events). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0459
  - The value must not be missing or empty
* - V0519
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0409
  - The document reference does not exist
```

### informationEnvironmentReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) detailing methodologies used for assessing how the levels of past adverse impacts or potential adverse consequences on the environment have been defined. References may include descriptions of approaches and available data used in the assessment. Note that generic approaches only are required (i.e. not related to specific flood events). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0460
  - The value must not be missing or empty
* - V0520
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0410
  - The document reference does not exist
```

### informationHumanHealthSocialReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide document(s) or link(s) detailing methodologies used for assessing how the levels of past adverse impacts or potential adverse consequences on human health have been defined. References may include descriptions of approaches and available data used in the assessment. Note that generic approaches only are required (i.e. not related to specific flood events). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0461
  - The value must not be missing or empty
* - V0521
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0411
  - The document reference does not exist
```

### otherRelevantInformationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to any other relevant available or readily derivable information used in the PFRA. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0522
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0412
  - The document reference does not exist
```
