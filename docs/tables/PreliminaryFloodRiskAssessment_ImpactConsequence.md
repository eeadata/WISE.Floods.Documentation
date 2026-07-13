# PreliminaryFloodRiskAssessment_ImpactConsequence

## Descripción

Preliminary Flood Risk Assessment - Impacts and Consequences

Uniqueness: floodEventCode + euFloodsHazardAreaCode + typeImpactConsequence + impactConsequenceCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - TU0424
  - Checks if euFloodsHazardAreaCode, floodEventCode, typeImpactConsequence and impactConsequenceCode are uniques within table
* - XC0423
  - The combination of floodEventCode+euFloodsHazardAreaCode is not a valid member of the PreliminaryFloodRiskAssessment\_FloodEventLocation table
* - XC0425
  - There must be at least one record for every euFloodsHazardAreaCode reported in table PreliminaryFloodRiskAssessment\_FloodEventLocation
```

### floodEventCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 42 characters. Required. Unique code for the flood event.
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
* - V0548
  - The value must not be missing or empty
* - V0549
  - The value is not a valid member of the referenced list.
```

### euFloodsHazardAreaCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 42 characters. Required. Unique code for the flood location - up to 42 characters in total. Can also be used as an identifier for multiple surface water bodies designated under the WFD which the flood location is represented by. A polygon must be reported as a representation of the flood location to establish link between spatial feature and information in xml schema.
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
* - V0490
  - The value must not be missing or empty
* - V0550
  - The value is not a valid member of the PreliminaryFloodRiskAssessment\_FloodEventLocation table
```

### typeImpactConsequence

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose a type of consequence impacting, from the 'TypeImpactConsequence' codelist values.
* - Field type
  - TypeImpactConsequence
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
* - V0475
  - The value does not exist in codelist ImpactConsequence.
* - V0498
  - The value must not be missing or empty
```

### impactConsequenceCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'ImpactConsequence' codelist values. Define relevant type of Consequences impacting on the chosen 'typeImpactConsequence' value. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ImpactConsequence
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
* - V0491
  - The value must not be missing or empty
* - V0497
  - The value does not exist in codelist ImpactConsequence
* - V0529
  - Duplicate values for impactConsequenceCode exist. The list of values needs to be distinct in each record.
```

### degreeTotalDamage

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. The total damage and loss cost in Euros for the flood event. Can also be reported as a range. The exemption types - 9999 = 'Unknown', -8888 = 'Yet to be measured' and -7777 = 'Not Applicable' can be used.
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
* - V0494
  - The value must be zero, greater than zero or one of the exception values: -9999, -8888 or -7777
```

### degreeTotalDamageClass

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Choose from the 'TotalDamageClass' codelist values. The total damage defined by the classes.
* - Field type
  - TotalDamageClass
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
* - V0544
  - The value does not exist in codelist TotalDamageClass.
```

### degreeTotalDamageGDP

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. The total damage in percentage of the total GDP for the flood event. Can also be reported as a range. The exemption types -9999 = 'Unknown', -8888 = 'Yet to be measured' and -7777 = 'Not Applicable' can be used.
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
* - V0495
  - The value must be zero, greater than zero or one of the exception values: -9999, -8888 or -7777
```

### fatalities

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Only for past floods. If possible, indicate number of individual fatalities as direct consequence of flood.
* - Field type
  - int
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
* - V0492
  - The value is not a valid whole number
* - V0551
  - The value should be a non-negative number.
```

### otherConsequenceDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Optional. Only to be used if the type is set to 'Other' in the enumeration list.
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
* - V0533
  - The length must be less than or equal to 1000
```

### otherDamageDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Optional. Other numerical measure indicative of degree of (potentially) adverse consequences.
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
* - V0534
  - The length must be less than or equal to 1000
```
