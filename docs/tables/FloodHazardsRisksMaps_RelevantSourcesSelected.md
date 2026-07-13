# FloodHazardsRisksMaps_RelevantSourcesSelected

## Descripción

Flood Hazards and Risks Maps - Relevant Sources of Flooding Selected
Description: RelevantSourcesSelected
This table relates to the sources of flooding considered relevant at the Unit of Management level and requires Member States to indicate whether a modelling approach has been used to develop the flood hazard and flood risk maps, while also providing the opportunity to supply further information on the specific type of model(s applied; in addition, the schema elements under this section cover the provision of information on whether the maps include different flooding probability scenarios.
Uniqueness: (controlled by QC). Explanation:
Possible relevant sources are:
- Fluvial.
- Pluvial.
- Sea water.
- Artificial water bearing infraestructure.
- Groundwater.
- Other source.
The combination euFloodsUnitOfManagementCode + relevantSource must be unique.

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - R0829
  - The combination euFloodsUnitOfManagementCode, relevantSource and relevantSourceOtherDescription must be unique if relevantSource is equal to 'other'
* - TU0809
  - The combination euFloodsUnitOfManagementCode and relevantSource must be unique
* - XC0820
  - There must be at least one record for every euFloodsUnitOfManagement reported in table FloodsHazardsRisksMaps
* - XC0833
  - The table FloodHazardsRisksMaps\_RelevantSourcesSelected does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0838
  - The table FloodHazardsRisksMaps\_RelevantSourcesSelected contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
```

### euFloodsUnitOfManagementCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 42 characters. Required. Unique EU code for the Unit of Management or WFD River Basin District. Add the two-letter ISO Country code to the Member State unique id - up to 42 characters in total. If unit of management is the same as the WFD RBD please use the EURBDCode as the unit of management.
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
* - V0869
  - The length must be less than or equal to 42
* - V0870
  - The value does not match the pattern to be used
* - V0943
  - The value must not be missing or empty
* - XC0818
  - euFloodsUnitOfManagementCode must exist on table FHRM
```

### relevantSourceOtherDescription

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
* - R0800
  - relevantSourcesOtherDescription must be reported if and only if the value of relevantSource is equal to 'other' on table FHRM\_RelevantSourcesSelected
* - R0823
  - relevantSourceOtherDescription must be reported if and only if relevantSource is 'other'
* - V0802
  - The length must be less than or equal to 1000
```

### relevantSource

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'SourceOfFlooding' codelist values. Indicate which sources of flooding are considered to be relevant to this UoM or RBD.
* - Field type
  - SourceOfFlooding
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
* - V0871
  - The value does not exist in codelist SourceOfFlooding
* - V0945
  - The value must not be missing or empty
* - V1807
  - The relevantSource value 'unknown' is not valid.
```

### modellingUsed

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Choose from the 'YesNo' codelist values. Indicate whether a modelling approach has been used to inform the development of the flood hazard and flood risk maps.
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
* - V0872
  - If reported, the value must exist in codelist YesNo
* - V1811
  - The value must not be missing or empty. [V1811]
```

### modellingNotUsedDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘No’ is selected from enumeration list to indicate a modelling approach has not been used, provide a description as to what approach has been used.
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
* - R0818
  - modellingNotUsedDescription must be reported if and only if modellingUsed is 'no'
* - V0873
  - The length must be less than or equal to 1000
```

### modellingUsedReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. Provide documents or links to relevant documents covering the following areas related to the modelling approach used: <ul> <li>the types of models used,</li> <li>the resolution of the models used,</li> <li>the key datasets used in the modelling process.</li> </ul> More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0819
  - modellingUsedReference must be reported if and only if modellingUsed is 'yes'
* - V0973
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0819
  - The document reference does not exist
```

### lowProbabilityScenarioElement

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. Choose from the 'ElementType' codelist values. Depending on which relevant source type of flooding is selected, indicate the different elements included in the hazard maps. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ElementType
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
* - V0874
  - The value does not exist in codelist ElementType
* - V0974
  - Duplicate values for lowProbabilityScenarioElement exist. The list of values needs to be distinct in each record.
```

### lowProbabilityScenarioElementOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ is selected in 'elementsLowProbability', provide a description.
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
* - R0820
  - lowProbabilityScenarioElementOther must be reported if and only if lowProbabilityScenarioElement is 'other'
* - V0875
  - The length must be less than or equal to 1000
```

### mediumProbabilityScenarioElement

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. Choose from the 'ElementType' codelist values. Depending on which relevant source type of flooding is selected, indicate the different elements included in the hazard maps. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ElementType
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
* - V0876
  - The value does not exist in codelist ElementType
* - V0941
  - The value must not be missing or empty
* - V0975
  - Duplicate values for mediumProbabilityScenarioElement exist. The list of values needs to be distinct in each record.
```

### mediumProbabilityScenarioElementOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected in 'elementsMediumProbability', provide a description.
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
* - R0821
  - mediumProbabilityScenarioElementOther must be reported if and only if mediumProbabilityScenarioElement is 'other'
* - V0877
  - The length must be less than or equal to 1000
```

### highProbabilityScenarioElement

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. Choose from the 'ElementType' codelist values. Depending on which relevant source type of flooding is selected, indicate the different elements included in the hazard maps. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ElementType
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
* - V0878
  - The value does not exist in codelist ElementType
* - V0976
  - Duplicate values for highProbabilityScenarioElement exist. The list of values needs to be distinct in each record.
```

### highProbabilityScenarioElementOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ is selected in elementsHighProbability, provide a description.
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
* - R0822
  - highProbabilityScenarioElementOther must be reported if and only if highProbabilityScenarioElement is 'other'
* - V0879
  - The length must be less than or equal to 1000
```
