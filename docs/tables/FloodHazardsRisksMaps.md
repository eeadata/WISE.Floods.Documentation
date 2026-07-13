# FloodHazardsRisksMaps

## Descripción

FHRM
Description: Flood Hazards and Risks Maps (FHRM)
Flood hazards maps - information on the geographical area which could be flooded under different scenarios (Article 6.3);
Flood risk maps – information on the potential adverse consequences of these flood scenarios (Article 6.5).

Uniqueness: euFloodsUnitOfManagementCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - TU0806
  - The field euFloodsUnitOfManagementCode must be unique within table
* - XC0832
  - The table FloodHazardsRisksMaps does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0837
  - The table FloodHazardsRisksMaps contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
```

### euFloodsUnitOfManagementCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V0818
  - The length must be less than or equal to 42
* - V0883
  - The value does not match the pattern to be used
* - V0898
  - The value must not be missing or empty
```

### mappingApproachReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide documents or links to relevant documents covering the following areas related to the approach used in the mapping of flood hazard and flood risk: In particular, please focus on the following areas: 1. Whether and how flood defences are considered; 2. Whether and how flood defence failure scenarios are considered; 3. Whether and how existing buildings and infrastructure are considered; 4. How uncertainty has been taken account of (what approach has been used to attempt to quantify uncertainty in the mapping of flood hazard and flood risk) Please note that 1 to 4 above may be covered in a single document in which case please be careful to Bookmark the relevant chapters, sections or page ranges. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0899
  - The value must not be missing or empty
* - V0961
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0826
  - The document reference does not exist
```

### sameSourcesAsAPSFR

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Indicate whether the sources mapped are the same as those considered in the APSFR. Areas for which flood hazard/risk maps should be prepared are indicated at the APSFR stage.
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

* - Código
  - Descripción
* - V0803
  - The value does not exist in codelist YesNo
* - V0900
  - The value must not be missing or empty
```

### sameSourcesAsAPSFRDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘No’ is selected from enumeration list in SameSourcesAsAPSFR ,provide an explanation as to why the sources mapped are different to those considered in the APSFR.
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

* - Código
  - Descripción
* - R0832
  - sameSourcesAsAPSFRDescription must be reported if sameSourcesAsAPSFR is 'No'
* - V0804
  - The length must be less than or equal to 1000
```

### returnPeriodsAndProbabilitiesApproach

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'ReturnPeriodAndProbabilitiesApproach' codelist values. Provide an indication of the approach taken to the calculation of flood return periods and probabilities. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ReturnPeriodAndProbabilitiesApproach
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - V0805
  - The value does not exist in codelist ReturnPeriodAndProbabilitiesApproach
* - V0901
  - The value must not be missing or empty
* - V0962
  - Duplicate values for returnPeriodsAndProbabilitiesApproach exist. The list of values needs to be distinct in each record.
```

### returnPeriodsAndProbabilitiesApproachExpertJudgementDescript

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R0833
  - returnPeriodsAndProbabilitiesApproachExpertJudgementDescription must be reported if returnPeriodsAndProbabilitiesApproach is 'expertJudgement'
* - V0806
  - The length must be less than or equal to 1000
```

### returnPeriodsAndProbabilitiesApproachOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ is selected from enumeration list provide a description as to why this is the case (it is acceptable to use ‘Uncertain’ but an explanation (however brief) is required).
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

* - Código
  - Descripción
* - R0834
  - returnPeriodsAndProbabilitiesApproachOther must be reported if returnPeriodsAndProbabilitiesApproach is 'other'
* - V0807
  - The length must be less than or equal to 1000
```

### returnPeriodsAndProbabilitiesApproachReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to the information relating to the approach taken to the calculation of flood return periods and probabilities. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0910
  - The value must not be missing or empty
* - V0963
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0803
  - The document reference does not exist
```

### article_6_2_PriorInformationExchangeOccurred

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. For International UOMs/RBDs state whether prior exchange of information has taken place in the preparation of flood hazard/flood risk maps for APSFRs which are shared with other MS or non-MS.
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

* - Código
  - Descripción
* - V0808
  - The value does not exist in codelist YesNo
* - V0903
  - The value must not be missing or empty
```

### article_6_2_PriorInformationExchangeDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘No’ selected in Article6.2PriorInformationExchangeOccurred, provide an explanation.
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

* - Código
  - Descripción
* - R0835
  - article\_6\_2\_PriorInformationExchangeDescription must be reported if article\_6\_2\_PriorInformationExchangeOccurred is 'No'
* - V0809
  - The length must be less than or equal to 1000
```

### article_6_2_PriorInformationExchange

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. Choose from the 'InternationalInformationExchange' codelist values. Where Article6.2PriorInformationExchangeOccured is 'Yes', indicate the mechanism of prior information exchange. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - R0836
  - article\_6\_2\_PriorInformationExchange must be reported if article\_6\_2\_PriorInformationExchangeOccurred is 'Yes'
* - V0810
  - The value does not exist in codelist InternationalInformationExchange
* - V0964
  - Duplicate values for article\_6\_2\_PriorInformationExchange exist. The list of values needs to be distinct in each record.
```

### article_6_2_PriorInformationExchangeOtherDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ is selected in 'Article6.2PriorInformationExchange', provide an explanation.
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

* - Código
  - Descripción
* - R0837
  - article\_6\_2\_PriorInformationExchangeOtherDescription must be reported if article\_6\_2\_PriorInformationExchange is 'other'
* - V0811
  - The length must be less than or equal to 1000
```

### article_6_2_PriorInformationExchangeReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to evidence that the coordination mechanisms are in place for prior information exchange. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0965
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0809
  - The document reference does not exist
```

### article_6_5_a_MethodInhabitantsAffectedReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to methods (including criteria) used to determine for each flood scenario the indicative number of inhabitants affected (art 6.5.a). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0904
  - The value must not be missing or empty
* - V0966
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0804
  - The document reference does not exist
```

### article_6_5_b_MethodEconomicActivityAffectedReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to methods (including criteria) used to determine for each flood scenario the type of economic activity affected (art 6.5.b). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0905
  - The value must not be missing or empty
* - V0967
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0805
  - The document reference does not exist
```

### article_6_5_c_MethodLocationIedInstallationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to methods (including criteria) used to determine for each flood scenario the location of the IED installation (art 6.5.c). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0906
  - The value must not be missing or empty
* - V0968
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0806
  - The document reference does not exist
```

### article_6_5_c_MethodWfdProtectedAreasReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to methods (including criteria) used to determine for each flood scenario the potential adverse consequences on WFD Protected Areas (art 6.5.c) More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0907
  - The value must not be missing or empty
* - V0969
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0807
  - The document reference does not exist
```

### article_6_5_d_MethodOtherInformationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to methods (including criteria) used to determine for each flood scenario the type of other information considered relevant by Member States (art 6.5.d). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0970
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0808
  - The document reference does not exist
```

### article_14_4_ClimateChange

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'ClimateChange' codelist values. Has climate change been taken into account in the mapping of flood hazard/risk?
* - Field type
  - ClimateChange
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - V0801
  - The value does not exist in codelist ClimateChange
* - V0908
  - The value must not be missing or empty
```

### article_14_4_ClimateChangeReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. If article\_14\_4\_ClimateChange=‘Yes’ provide document(s) or link(s) detailing how climate change has (or links to a document providing an explanation if it has not) been taken into account in the assessment of flood hazard/risk. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - R0831
  - article\_14\_4\_ClimateChangeReference must be reported if article\_14\_4\_ClimateChange has been reported as 'Yes'
* - V0971
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0802
  - The document reference does not exist
```

### mapExplanationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to information that gives an explanation (to be made available to the public through WISE) on how to understand the flood maps in terms of contents, scale, purpose/use, accuracy, legends, date of publication, responsible authorities and links to further information. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0909
  - The value must not be missing or empty
* - V0972
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0801
  - The document reference does not exist
```
