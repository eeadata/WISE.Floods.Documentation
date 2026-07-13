# FloodRiskManagementPlans_Summary

## Descripción

Flood Risk Management Plans - Summary
This table relates to summary information at the Unit of Management (UoM) level, covering the prioritisation of measures, references to achieving the objectives, coordination between Flood Risk Management Plans and River Basin Management Plans, national and international coordination, relevant aspects set out under Article 7 such as the consideration of climate change impacts, public participation and consultation mechanisms, and cost–benefit analyses of measures.
Uniqueness: euFloodsUnitOfManagementCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - XC0627
  - The table FloodRiskManagementPlans\_Summary does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0630
  - The table FloodRiskManagementPlans\_Summary contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - TU0605
  - The field euFloodsUntOfManagementCode must be unique within table
* - V0623
  - The length must be less than or equal to 42
* - V0624
  - The value does not match the pattern to be used
* - V0659
  - The value must not be missing or empty
```

### objectivesReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide a reference to explain how measures contribute to achieving the objectives within the FRMP. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0660
  - The value must not be missing or empty
* - V0681
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0609
  - The document reference does not exist
```

### summaryPriorityMethodologyReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide reference(s) to explanation in support of the level of priority for the measure. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0682
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0610
  - The document reference does not exist
```

### localNationalInternationalCoordination

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose an indication of the level of local and or national or international coordination from the 'LocalNationalInternationalCoordination' codelist values. More than one option can be selected. If any is added, provide a reference document or link in the 'LocalNationalInternationalCoordinationReference' schema; if no one, provide a reason/description (text) in 'LocalNationalInternationalCoordinationDescription'. If more than one value is selected, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - LocalNationalInternationalCoordination
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
* - R0626
  - if 'localNationalInternationalCoordination' has value 'noNeed' or 'noCoordination', no other option can be selected
* - V0631
  - The value does not exist in codelist LocalNationalInternationalCoordination
* - V0667
  - The value must not be missing or empty
* - V0683
  - Duplicate values for localNationalInternationalCoordination exist. The list of values needs to be distinct in each record.
```

### localNationalInternationalCoordinationDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. Provide a reason/description if 'LocalNationalInternationalCoordination' is set to 'No Coordination has taken place'
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
* - R0608
  - localNationalInternationalCoordinationDescription must not be reported if localNationalInternationalCoordination doesn't contain 'noCoordination' as an option
* - R0609
  - localNationalInternationalCoordinationDescription must be reported if localNationalInternationalCoordination contains 'noCoordination' as an option
* - V0632
  - The length must be less than or equal to 1000
```

### localNationalInternationalCoordinationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. If any item other than 'No Coordination has taken place' has been selected provide document(s) or link(s) to relevant documents describing the coordination process and approach. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0610
  - localNationalInternationalCoordinationReference must not be reported if localNationalInternationalCoordination contains 'noCoordination' as an option
* - R0611
  - localNationalInternationalCoordinationReference must be reported if localNationalInternationalCoordination doesn't contain 'noCoordination' as an option
* - V0684
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0613
  - The document reference does not exist
```

### climateChangeImpacts

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose if the impact of climate change on the occurrence of floods has been taken into consideration within the FRMP from the 'YesNo' codelist values. If 'Yes', provide a reference document or link in the SummaryClimateChange/Reference schema to relevant documentation for example on measures taken to mitigate the expected effects of climate change on the likelihood and potential adverse effects of flooding; if 'No', provide a reason/description (text) in the SummaryClimateChange /Justification schema.
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
* - V0622
  - The value does not exist in codelist YesNo
* - V0661
  - The value must not be missing or empty
```

### climateChangeImpactsDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters Conditional. Provide a reason/description if 'climateChangeImpacts' is set to 'No'
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
* - R0612
  - climateChangeImpactsDescription must not be reported if climateChangeImpacts is 'yes'
* - R0613
  - climateChangeImpactsDescription must be reported if climateChangeImpacts is 'no'
* - V0633
  - The length must be less than or equal to 1000
```

### climateChangeImpactsReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. If climateChangeImpacts is set to 'Yes' provide document(s) or link(s) to relevant documents describing how the impact of climate change on the occurrence of floods been taken into consideration within the FRMP. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0614
  - climateChangeImpactsReference must be reported if climateChangeImpacts is 'yes'
* - R0615
  - climateChangeImpactsReference must not be reported if climateChangeImpacts is 'no'
* - V0685
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0614
  - The document reference does not exist
```

### impactPublicParticipation

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose one or more indication(s) of the impact of public participation on the final outcome of the plans from the 'ImpactPublicParticipation' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ImpactPublicParticipation
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
* - V0640
  - The value does not exist in codelist ImpactPublicParticipation
* - V0668
  - The value must not be missing or empty
* - V0686
  - Duplicate values for impactPublicParticipation exist. The list of values needs to be distinct in each record.
```

### impactPublicParticipationOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' selected from enumeration list, provide a description of the other outcome(s) that stakeholder engagement had on the plans groups of stakeholders actively involved in the development of the flood risk management plans.
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
* - R0620
  - impactPublicParticipationOther must not be reported if impactPublicParticipation doesn't include 'other' as an option
* - R0621
  - impactPublicParticipationOther must be reported if impactPublicParticipation includes 'other' as an option
* - V0636
  - The length must be less than or equal to 1000
```

### article_7_2_Reference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide documents or links to relevant documents covering the following areas related to objectives: <ul> <li>details of the objectives set and how they meet the requirements of Article 7.2 of the FD,</li> <li>how the objectives relate to impacts on human health, the environment, cultural heritage and economic activity in terms of making them measureable (e.g. number of residential properties at risk),</li> <li>the processes for both developing the objectives and selecting and prioritising measures to achieve the stated objectives.</li> </ul> More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0662
  - The value must not be missing or empty
* - V0687
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0608
  - The document reference does not exist
```

### article_7_3_SummaryAspects

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Choose what aspects are taken into account by your flood risk management plans from the 'AspectsIncluded' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - AspectsIncluded
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
* - V0627
  - The value does not exist in codelist AspectsIncluded
* - V0688
  - Duplicate values for article\_7\_3\_SummaryAspects exist. The list of values needs to be distinct in each record.
```

### article_7_3_SummaryAspectsDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 2000 characters. Conditional. If one or more aspects from the list 'Article7.3SummaryAspects' are not selected, provide a reason for this.
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
* - R0604
  - article\_7\_3\_SummaryAspectsDescription must not be reported if article\_7\_3\_SummaryAspects is reported
* - R0605
  - article\_7\_3\_SummaryAspectsDescription must be reported if article\_7\_3\_SummaryAspects is not reported
* - V0628
  - The length must be less than or equal to 2000
```

### article_9_2_CoordinationFRMPandRBMP

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Indicate how the development of the FRMPs have been coordinated with the development of the River Basin Management Plan for the WFD from the 'CoordinationFRMPandRBMP' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - CoordinationFRMPandRBMP
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
* - V0629
  - The value does not exist in codelist CoordinationFRMPandRBMP
* - V0669
  - The value must not be missing or empty
* - V0689
  - Duplicate values for article\_9\_2\_CoordinationFRMPandRBMP exist. The list of values needs to be distinct in each record.
```

### article_9_2_CoordinationFRMPandRBMPOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' selected from enumeration list, provide a description of the other ways development of the FRMPs have been coordinated with the development of the River Basin Management Plans for the WFD.
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
* - R0606
  - article\_9\_2\_CoordinationFRMPandRBMPOther must not be reported if article\_9\_2\_CoordinationFRMPandRBMP doesn't contain 'other' as an option
* - R0607
  - article\_9\_2\_CoordinationFRMPandRBMPOther must be reported if article\_9\_2\_CoordinationFRMPandRBMP contains 'other' as an option
* - V0630
  - The length must be less than or equal to 1000
```

### article_9_2_CoordinationFRMPandRBMPReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to relevant documents referring to how the development of the FRMP has been coordinated with the development of the second River Basin Management Plan. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0663
  - The value must not be missing or empty
* - V0690
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0612
  - The document reference does not exist
```

### article_10_1_PublicConsultationsMechanisms

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide information as to the mechanism(s) used for informing public and interested parties about the consultation process from the 'PublicConsultationsMechanisms' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - PublicConsultationsMechanisms
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
* - V0638
  - The value does not exist in codelist PublicConsultationsMechanisms
* - V0670
  - The value must not be missing or empty
* - V0691
  - Duplicate values for article\_10\_1\_PublicConsultationsMechanisms exist. The list of values needs to be distinct in each record.
```

### article_10_1_PublicConsultationsMechanismsOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from the enumeration list, provide a description of the other mechanisms used for informing the public and other interested parties about the consultation process.
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
* - R0616
  - article\_10\_1\_PublicConsultationsMechanismsOther must not be reported if article\_10\_1\_PublicConsultationsMechanisms doesn't include 'other' as an option
* - R0617
  - article\_10\_1\_PublicConsultationsMechanismsOther must be reported if article\_10\_1\_PublicConsultationsMechanisms contains 'other' as an option
* - V0635
  - The length must be less than or equal to 1000
```

### article_10_2_ConsultationStakeholdersInvolved

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide information as to the groups of stakeholders who have been actively involved in the development of the flood risk management plans from the 'ConsultationStakeholdersInvolved' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ConsultationStakeholdersInvolved
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
* - V0639
  - The value does not exist in codelist ConsultationStakeholdersInvolved
* - V0671
  - The value must not be missing or empty
* - V0692
  - Duplicate values for article\_10\_2\_ConsultationStakeholdersInvolved exist. The list of values needs to be distinct in each record.
```

### article_10_2_ConsultationStakeholdersInvolvedOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from enumeration list, provide a description of the other outcome(s) that stakeholder engagement had on the plans groups of stakeholders actively involved in the development of the flood risk management plans.
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
* - R0618
  - article\_10\_2\_ConsultationStakeholdersInvolvedOther must not be reported if article\_10\_2\_ConsultationStakeholdersInvolved doesn't contain 'other' as an option
* - R0619
  - article\_10\_2\_ConsultationStakeholdersInvolvedOther must be reported if article\_10\_2\_ConsultationStakeholdersInvolved includes 'other' as an option
* - V0708
  - The length must be less than or equal to 1000
```

### article_10_2_ConsultationStakeholdersInvolvedMechanisms

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose the mechanism(s) used to encourage the active involvement of stakeholders from the 'ConsultationsStakeholdersInvolvedMechanisms' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - ConsultationStakeholdersInvolvedMechanisms
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
* - V0641
  - The value does not exist in codelist ConsultationStakeholdersInvolvedMechanisms
* - V0672
  - The value must not be missing or empty
* - V0693
  - Duplicate values for article\_10\_2\_ConsultationStakeholdersInvolvedMechanisms exist. The list of values needs to be distinct in each record.
```

### article_10_2_ConsultationStakeholdersInvolvedMechanismsOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from the enumeration list, provide a description of the other mechanisms used to encourage the active involvement of stakeholders.
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
* - R0622
  - article\_10\_2\_ConsultationStakeholdersInvolvedMechanismsOther must not be reported if article\_10\_2\_ConsultationStakeholdersInvolvedMechanisms doesn't include 'other' as an option
* - R0623
  - article\_10\_2\_ConsultationStakeholdersInvolvedMechanismsOther must be reported if article\_10\_2\_ConsultationStakeholdersInvolvedMechanisms contains 'other' a an option
* - V0637
  - The length must be less than or equal to 1000
```

### annex_A1_5_SummaryCostBenefitReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. If under the schema element above: FRMP/SummaryOverall/SummaryAspects/AnnexAspectsIncluded 'For shared river basins a description of the cost-benefit analysis used to assess measures with transnational effects (Y/N)' 'Yes' is selected, provide document(s) or link(s) to relevant documents including a description of the methodology of cost-benefit analysis used to assess measures with transnational effects. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0603
  - It must be reported if annexAspectsIncluded contains "costBenefits" as an option. Otherwise, it should not be reported.
* - V0694
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0611
  - The document reference does not exist
```

### annexAspectsIncluded

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Choose the plan(s) your flood risk management plan takes into account from the 'AnnexAspectsIncluded' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - AnnexAspectsIncluded
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
* - V0625
  - The value does not exist in codelist AnnexAspectsIncluded
* - V0695
  - Duplicate values for annexAspectsIncluded exist. The list of values needs to be distinct in each record.
```

### annexAspectsIncludedDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 2000 characters. Conditional. If any item has not been selected from the enumeration list above ('No' has been selected), please provide a reason for this.
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
* - R0601
  - annexAspectsIncludedDescription must not be reported if annexAspectsIncluded is reported
* - R0602
  - annexAspectsIncludedDescription must be reported if annexAspectsIncluded is not reported
* - V0626
  - The length must be less than or equal to 2000
```

### stakeholderConsultationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to relevant documentation on public information and consultation and on stakeholder engagement. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0664
  - The value must not be missing or empty
* - V0696
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0615
  - The document reference does not exist
```

### changesReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to relevant documentation describing any changes or updates since the publication of the previous version of the FRMP in accordance with Article 14(3) which includes the requirement for a review and update of the FRMPs every six years. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0665
  - The value must not be missing or empty
* - V0697
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0616
  - The document reference does not exist
```

### frmpProgressReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide document(s) or link(s) to relevant documentation of progress made toward achievement of the objectives referred to in Article 7.2 - a description of, and explanation for, any measures foreseen in the earlier version of the FRMP which were planned to be undertaken and have not been taken forward (Annex, part B.2 and 3). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0666
  - The value must not be missing or empty
* - V0698
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0617
  - The document reference does not exist
```

### additionalMeasuresReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to relevant documentation on any additional measures put in place since publication of the previous version of the FRMP (Annex, part B.4). If the information requested by this schema element is not provided it will be presumed that no additional measures have been adopted since the publication of the previous FRMPs. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0699
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0618
  - The document reference does not exist
```

### progressReviewDescriptionReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide reference(s) to the progress made with implementation of measures and include a timetable for completion where possible. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0700
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0619
  - The document reference does not exist
```

### supportingInformationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Please provide reference(s) to more detailed supporting documents (e.g. full FRMP, methodology documents and external sources of information) or other relevant information not already covered in the preceding reference schemas. These documents should be uploaded to the EIONET. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0701
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0620
  - The document reference does not exist
```
