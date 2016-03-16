#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 on 2016-03-16.
#  2016, SMART Health IT.

from . import element


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_name, jsondict):
        """ Instantiate a resource of the type correlating to "resource_name".
        
        :param str resource_name: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        if "Account" == resource_name:
            from . import account
            return account.Account(jsondict)
        if "ActionDefinition" == resource_name:
            from . import actiondefinition
            return actiondefinition.ActionDefinition(jsondict)
        if "ActionDefinitionBehavior" == resource_name:
            from . import actiondefinition
            return actiondefinition.ActionDefinitionBehavior(jsondict)
        if "ActionDefinitionCustomization" == resource_name:
            from . import actiondefinition
            return actiondefinition.ActionDefinitionCustomization(jsondict)
        if "Address" == resource_name:
            from . import address
            return address.Address(jsondict)
        if "Age" == resource_name:
            from . import age
            return age.Age(jsondict)
        if "AllergyIntolerance" == resource_name:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntolerance(jsondict)
        if "AllergyIntoleranceReaction" == resource_name:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntoleranceReaction(jsondict)
        if "Annotation" == resource_name:
            from . import annotation
            return annotation.Annotation(jsondict)
        if "Appointment" == resource_name:
            from . import appointment
            return appointment.Appointment(jsondict)
        if "AppointmentParticipant" == resource_name:
            from . import appointment
            return appointment.AppointmentParticipant(jsondict)
        if "AppointmentResponse" == resource_name:
            from . import appointmentresponse
            return appointmentresponse.AppointmentResponse(jsondict)
        if "Attachment" == resource_name:
            from . import attachment
            return attachment.Attachment(jsondict)
        if "AuditEvent" == resource_name:
            from . import auditevent
            return auditevent.AuditEvent(jsondict)
        if "AuditEventAgent" == resource_name:
            from . import auditevent
            return auditevent.AuditEventAgent(jsondict)
        if "AuditEventAgentNetwork" == resource_name:
            from . import auditevent
            return auditevent.AuditEventAgentNetwork(jsondict)
        if "AuditEventEntity" == resource_name:
            from . import auditevent
            return auditevent.AuditEventEntity(jsondict)
        if "AuditEventEntityDetail" == resource_name:
            from . import auditevent
            return auditevent.AuditEventEntityDetail(jsondict)
        if "AuditEventSource" == resource_name:
            from . import auditevent
            return auditevent.AuditEventSource(jsondict)
        if "BackboneElement" == resource_name:
            from . import backboneelement
            return backboneelement.BackboneElement(jsondict)
        if "Basic" == resource_name:
            from . import basic
            return basic.Basic(jsondict)
        if "Binary" == resource_name:
            from . import binary
            return binary.Binary(jsondict)
        if "BodySite" == resource_name:
            from . import bodysite
            return bodysite.BodySite(jsondict)
        if "Bundle" == resource_name:
            from . import bundle
            return bundle.Bundle(jsondict)
        if "BundleEntry" == resource_name:
            from . import bundle
            return bundle.BundleEntry(jsondict)
        if "BundleEntryRequest" == resource_name:
            from . import bundle
            return bundle.BundleEntryRequest(jsondict)
        if "BundleEntryResponse" == resource_name:
            from . import bundle
            return bundle.BundleEntryResponse(jsondict)
        if "BundleEntrySearch" == resource_name:
            from . import bundle
            return bundle.BundleEntrySearch(jsondict)
        if "BundleLink" == resource_name:
            from . import bundle
            return bundle.BundleLink(jsondict)
        if "CarePlan" == resource_name:
            from . import careplan
            return careplan.CarePlan(jsondict)
        if "CarePlanActivity" == resource_name:
            from . import careplan
            return careplan.CarePlanActivity(jsondict)
        if "CarePlanActivityDetail" == resource_name:
            from . import careplan
            return careplan.CarePlanActivityDetail(jsondict)
        if "CarePlanParticipant" == resource_name:
            from . import careplan
            return careplan.CarePlanParticipant(jsondict)
        if "CarePlanRelatedPlan" == resource_name:
            from . import careplan
            return careplan.CarePlanRelatedPlan(jsondict)
        if "CareTeam" == resource_name:
            from . import careteam
            return careteam.CareTeam(jsondict)
        if "CareTeamParticipant" == resource_name:
            from . import careteam
            return careteam.CareTeamParticipant(jsondict)
        if "Claim" == resource_name:
            from . import claim
            return claim.Claim(jsondict)
        if "ClaimCoverage" == resource_name:
            from . import claim
            return claim.ClaimCoverage(jsondict)
        if "ClaimDiagnosis" == resource_name:
            from . import claim
            return claim.ClaimDiagnosis(jsondict)
        if "ClaimItem" == resource_name:
            from . import claim
            return claim.ClaimItem(jsondict)
        if "ClaimItemDetail" == resource_name:
            from . import claim
            return claim.ClaimItemDetail(jsondict)
        if "ClaimItemDetailSubDetail" == resource_name:
            from . import claim
            return claim.ClaimItemDetailSubDetail(jsondict)
        if "ClaimItemProsthesis" == resource_name:
            from . import claim
            return claim.ClaimItemProsthesis(jsondict)
        if "ClaimMissingTeeth" == resource_name:
            from . import claim
            return claim.ClaimMissingTeeth(jsondict)
        if "ClaimPayee" == resource_name:
            from . import claim
            return claim.ClaimPayee(jsondict)
        if "ClaimProcedure" == resource_name:
            from . import claim
            return claim.ClaimProcedure(jsondict)
        if "ClaimRelated" == resource_name:
            from . import claim
            return claim.ClaimRelated(jsondict)
        if "ClaimResponse" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponse(jsondict)
        if "ClaimResponseAddItem" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItem(jsondict)
        if "ClaimResponseAddItemAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemAdjudication(jsondict)
        if "ClaimResponseAddItemDetail" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetail(jsondict)
        if "ClaimResponseAddItemDetailAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetailAdjudication(jsondict)
        if "ClaimResponseCoverage" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseCoverage(jsondict)
        if "ClaimResponseError" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseError(jsondict)
        if "ClaimResponseItem" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItem(jsondict)
        if "ClaimResponseItemAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemAdjudication(jsondict)
        if "ClaimResponseItemDetail" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetail(jsondict)
        if "ClaimResponseItemDetailAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailAdjudication(jsondict)
        if "ClaimResponseItemDetailSubDetail" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict)
        if "ClaimResponseItemDetailSubDetailAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetailAdjudication(jsondict)
        if "ClaimResponseNote" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseNote(jsondict)
        if "ClinicalImpression" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpression(jsondict)
        if "ClinicalImpressionFinding" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionFinding(jsondict)
        if "ClinicalImpressionInvestigations" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionInvestigations(jsondict)
        if "ClinicalImpressionRuledOut" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionRuledOut(jsondict)
        if "CodeSystem" == resource_name:
            from . import codesystem
            return codesystem.CodeSystem(jsondict)
        if "CodeSystemConcept" == resource_name:
            from . import codesystem
            return codesystem.CodeSystemConcept(jsondict)
        if "CodeSystemConceptDesignation" == resource_name:
            from . import codesystem
            return codesystem.CodeSystemConceptDesignation(jsondict)
        if "CodeSystemConceptProperty" == resource_name:
            from . import codesystem
            return codesystem.CodeSystemConceptProperty(jsondict)
        if "CodeSystemContact" == resource_name:
            from . import codesystem
            return codesystem.CodeSystemContact(jsondict)
        if "CodeSystemFilter" == resource_name:
            from . import codesystem
            return codesystem.CodeSystemFilter(jsondict)
        if "CodeSystemProperty" == resource_name:
            from . import codesystem
            return codesystem.CodeSystemProperty(jsondict)
        if "CodeableConcept" == resource_name:
            from . import codeableconcept
            return codeableconcept.CodeableConcept(jsondict)
        if "Coding" == resource_name:
            from . import coding
            return coding.Coding(jsondict)
        if "Communication" == resource_name:
            from . import communication
            return communication.Communication(jsondict)
        if "CommunicationPayload" == resource_name:
            from . import communication
            return communication.CommunicationPayload(jsondict)
        if "CommunicationRequest" == resource_name:
            from . import communicationrequest
            return communicationrequest.CommunicationRequest(jsondict)
        if "CommunicationRequestPayload" == resource_name:
            from . import communicationrequest
            return communicationrequest.CommunicationRequestPayload(jsondict)
        if "CompartmentDefinition" == resource_name:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinition(jsondict)
        if "CompartmentDefinitionContact" == resource_name:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinitionContact(jsondict)
        if "CompartmentDefinitionResource" == resource_name:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinitionResource(jsondict)
        if "Composition" == resource_name:
            from . import composition
            return composition.Composition(jsondict)
        if "CompositionAttester" == resource_name:
            from . import composition
            return composition.CompositionAttester(jsondict)
        if "CompositionEvent" == resource_name:
            from . import composition
            return composition.CompositionEvent(jsondict)
        if "CompositionSection" == resource_name:
            from . import composition
            return composition.CompositionSection(jsondict)
        if "ConceptMap" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMap(jsondict)
        if "ConceptMapContact" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapContact(jsondict)
        if "ConceptMapElement" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapElement(jsondict)
        if "ConceptMapElementTarget" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapElementTarget(jsondict)
        if "ConceptMapElementTargetDependsOn" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapElementTargetDependsOn(jsondict)
        if "Condition" == resource_name:
            from . import condition
            return condition.Condition(jsondict)
        if "ConditionEvidence" == resource_name:
            from . import condition
            return condition.ConditionEvidence(jsondict)
        if "ConditionStage" == resource_name:
            from . import condition
            return condition.ConditionStage(jsondict)
        if "Conformance" == resource_name:
            from . import conformance
            return conformance.Conformance(jsondict)
        if "ConformanceContact" == resource_name:
            from . import conformance
            return conformance.ConformanceContact(jsondict)
        if "ConformanceDocument" == resource_name:
            from . import conformance
            return conformance.ConformanceDocument(jsondict)
        if "ConformanceImplementation" == resource_name:
            from . import conformance
            return conformance.ConformanceImplementation(jsondict)
        if "ConformanceMessaging" == resource_name:
            from . import conformance
            return conformance.ConformanceMessaging(jsondict)
        if "ConformanceMessagingEndpoint" == resource_name:
            from . import conformance
            return conformance.ConformanceMessagingEndpoint(jsondict)
        if "ConformanceMessagingEvent" == resource_name:
            from . import conformance
            return conformance.ConformanceMessagingEvent(jsondict)
        if "ConformanceRest" == resource_name:
            from . import conformance
            return conformance.ConformanceRest(jsondict)
        if "ConformanceRestInteraction" == resource_name:
            from . import conformance
            return conformance.ConformanceRestInteraction(jsondict)
        if "ConformanceRestOperation" == resource_name:
            from . import conformance
            return conformance.ConformanceRestOperation(jsondict)
        if "ConformanceRestResource" == resource_name:
            from . import conformance
            return conformance.ConformanceRestResource(jsondict)
        if "ConformanceRestResourceInteraction" == resource_name:
            from . import conformance
            return conformance.ConformanceRestResourceInteraction(jsondict)
        if "ConformanceRestResourceSearchParam" == resource_name:
            from . import conformance
            return conformance.ConformanceRestResourceSearchParam(jsondict)
        if "ConformanceRestSecurity" == resource_name:
            from . import conformance
            return conformance.ConformanceRestSecurity(jsondict)
        if "ConformanceRestSecurityCertificate" == resource_name:
            from . import conformance
            return conformance.ConformanceRestSecurityCertificate(jsondict)
        if "ConformanceSoftware" == resource_name:
            from . import conformance
            return conformance.ConformanceSoftware(jsondict)
        if "ContactPoint" == resource_name:
            from . import contactpoint
            return contactpoint.ContactPoint(jsondict)
        if "Contract" == resource_name:
            from . import contract
            return contract.Contract(jsondict)
        if "ContractAgent" == resource_name:
            from . import contract
            return contract.ContractAgent(jsondict)
        if "ContractFriendly" == resource_name:
            from . import contract
            return contract.ContractFriendly(jsondict)
        if "ContractLegal" == resource_name:
            from . import contract
            return contract.ContractLegal(jsondict)
        if "ContractRule" == resource_name:
            from . import contract
            return contract.ContractRule(jsondict)
        if "ContractSigner" == resource_name:
            from . import contract
            return contract.ContractSigner(jsondict)
        if "ContractTerm" == resource_name:
            from . import contract
            return contract.ContractTerm(jsondict)
        if "ContractTermAgent" == resource_name:
            from . import contract
            return contract.ContractTermAgent(jsondict)
        if "ContractTermValuedItem" == resource_name:
            from . import contract
            return contract.ContractTermValuedItem(jsondict)
        if "ContractValuedItem" == resource_name:
            from . import contract
            return contract.ContractValuedItem(jsondict)
        if "Count" == resource_name:
            from . import count
            return count.Count(jsondict)
        if "Coverage" == resource_name:
            from . import coverage
            return coverage.Coverage(jsondict)
        if "DataElement" == resource_name:
            from . import dataelement
            return dataelement.DataElement(jsondict)
        if "DataElementContact" == resource_name:
            from . import dataelement
            return dataelement.DataElementContact(jsondict)
        if "DataElementMapping" == resource_name:
            from . import dataelement
            return dataelement.DataElementMapping(jsondict)
        if "DataRequirement" == resource_name:
            from . import datarequirement
            return datarequirement.DataRequirement(jsondict)
        if "DataRequirementCodeFilter" == resource_name:
            from . import datarequirement
            return datarequirement.DataRequirementCodeFilter(jsondict)
        if "DataRequirementDateFilter" == resource_name:
            from . import datarequirement
            return datarequirement.DataRequirementDateFilter(jsondict)
        if "DecisionSupportRule" == resource_name:
            from . import decisionsupportrule
            return decisionsupportrule.DecisionSupportRule(jsondict)
        if "DecisionSupportServiceModule" == resource_name:
            from . import decisionsupportservicemodule
            return decisionsupportservicemodule.DecisionSupportServiceModule(jsondict)
        if "DetectedIssue" == resource_name:
            from . import detectedissue
            return detectedissue.DetectedIssue(jsondict)
        if "DetectedIssueMitigation" == resource_name:
            from . import detectedissue
            return detectedissue.DetectedIssueMitigation(jsondict)
        if "Device" == resource_name:
            from . import device
            return device.Device(jsondict)
        if "DeviceComponent" == resource_name:
            from . import devicecomponent
            return devicecomponent.DeviceComponent(jsondict)
        if "DeviceComponentProductionSpecification" == resource_name:
            from . import devicecomponent
            return devicecomponent.DeviceComponentProductionSpecification(jsondict)
        if "DeviceMetric" == resource_name:
            from . import devicemetric
            return devicemetric.DeviceMetric(jsondict)
        if "DeviceMetricCalibration" == resource_name:
            from . import devicemetric
            return devicemetric.DeviceMetricCalibration(jsondict)
        if "DeviceUseRequest" == resource_name:
            from . import deviceuserequest
            return deviceuserequest.DeviceUseRequest(jsondict)
        if "DeviceUseStatement" == resource_name:
            from . import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict)
        if "DiagnosticOrder" == resource_name:
            from . import diagnosticorder
            return diagnosticorder.DiagnosticOrder(jsondict)
        if "DiagnosticOrderEvent" == resource_name:
            from . import diagnosticorder
            return diagnosticorder.DiagnosticOrderEvent(jsondict)
        if "DiagnosticOrderItem" == resource_name:
            from . import diagnosticorder
            return diagnosticorder.DiagnosticOrderItem(jsondict)
        if "DiagnosticReport" == resource_name:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict)
        if "DiagnosticReportImage" == resource_name:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReportImage(jsondict)
        if "Distance" == resource_name:
            from . import distance
            return distance.Distance(jsondict)
        if "DocumentManifest" == resource_name:
            from . import documentmanifest
            return documentmanifest.DocumentManifest(jsondict)
        if "DocumentManifestContent" == resource_name:
            from . import documentmanifest
            return documentmanifest.DocumentManifestContent(jsondict)
        if "DocumentManifestRelated" == resource_name:
            from . import documentmanifest
            return documentmanifest.DocumentManifestRelated(jsondict)
        if "DocumentReference" == resource_name:
            from . import documentreference
            return documentreference.DocumentReference(jsondict)
        if "DocumentReferenceContent" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceContent(jsondict)
        if "DocumentReferenceContext" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceContext(jsondict)
        if "DocumentReferenceContextRelated" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceContextRelated(jsondict)
        if "DocumentReferenceRelatesTo" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict)
        if "DomainResource" == resource_name:
            from . import domainresource
            return domainresource.DomainResource(jsondict)
        if "Duration" == resource_name:
            from . import duration
            return duration.Duration(jsondict)
        if "Element" == resource_name:
            from . import element
            return element.Element(jsondict)
        if "ElementDefinition" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinition(jsondict)
        if "ElementDefinitionBase" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBase(jsondict)
        if "ElementDefinitionBinding" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBinding(jsondict)
        if "ElementDefinitionConstraint" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionConstraint(jsondict)
        if "ElementDefinitionMapping" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionMapping(jsondict)
        if "ElementDefinitionSlicing" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicing(jsondict)
        if "ElementDefinitionType" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionType(jsondict)
        if "EligibilityRequest" == resource_name:
            from . import eligibilityrequest
            return eligibilityrequest.EligibilityRequest(jsondict)
        if "EligibilityResponse" == resource_name:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponse(jsondict)
        if "EligibilityResponseBenefitBalance" == resource_name:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponseBenefitBalance(jsondict)
        if "EligibilityResponseBenefitBalanceFinancial" == resource_name:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponseBenefitBalanceFinancial(jsondict)
        if "EligibilityResponseError" == resource_name:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponseError(jsondict)
        if "Encounter" == resource_name:
            from . import encounter
            return encounter.Encounter(jsondict)
        if "EncounterHospitalization" == resource_name:
            from . import encounter
            return encounter.EncounterHospitalization(jsondict)
        if "EncounterLocation" == resource_name:
            from . import encounter
            return encounter.EncounterLocation(jsondict)
        if "EncounterParticipant" == resource_name:
            from . import encounter
            return encounter.EncounterParticipant(jsondict)
        if "EncounterStatusHistory" == resource_name:
            from . import encounter
            return encounter.EncounterStatusHistory(jsondict)
        if "EnrollmentRequest" == resource_name:
            from . import enrollmentrequest
            return enrollmentrequest.EnrollmentRequest(jsondict)
        if "EnrollmentResponse" == resource_name:
            from . import enrollmentresponse
            return enrollmentresponse.EnrollmentResponse(jsondict)
        if "EpisodeOfCare" == resource_name:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCare(jsondict)
        if "EpisodeOfCareCareTeam" == resource_name:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareCareTeam(jsondict)
        if "EpisodeOfCareStatusHistory" == resource_name:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareStatusHistory(jsondict)
        if "ExpansionProfile" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfile(jsondict)
        if "ExpansionProfileCodeSystem" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileCodeSystem(jsondict)
        if "ExpansionProfileCodeSystemExclude" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileCodeSystemExclude(jsondict)
        if "ExpansionProfileCodeSystemExcludeCodeSystem" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileCodeSystemExcludeCodeSystem(jsondict)
        if "ExpansionProfileCodeSystemInclude" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileCodeSystemInclude(jsondict)
        if "ExpansionProfileCodeSystemIncludeCodeSystem" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileCodeSystemIncludeCodeSystem(jsondict)
        if "ExpansionProfileContact" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileContact(jsondict)
        if "ExpansionProfileDesignation" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignation(jsondict)
        if "ExpansionProfileDesignationExclude" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationExclude(jsondict)
        if "ExpansionProfileDesignationExcludeDesignation" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationExcludeDesignation(jsondict)
        if "ExpansionProfileDesignationInclude" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationInclude(jsondict)
        if "ExpansionProfileDesignationIncludeDesignation" == resource_name:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationIncludeDesignation(jsondict)
        if "ExplanationOfBenefit" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefit(jsondict)
        if "ExplanationOfBenefitAddItem" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItem(jsondict)
        if "ExplanationOfBenefitAddItemAdjudication" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemAdjudication(jsondict)
        if "ExplanationOfBenefitAddItemDetail" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetail(jsondict)
        if "ExplanationOfBenefitAddItemDetailAdjudication" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetailAdjudication(jsondict)
        if "ExplanationOfBenefitBenefitBalance" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalance(jsondict)
        if "ExplanationOfBenefitBenefitBalanceFinancial" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial(jsondict)
        if "ExplanationOfBenefitCoverage" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitCoverage(jsondict)
        if "ExplanationOfBenefitDiagnosis" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitDiagnosis(jsondict)
        if "ExplanationOfBenefitItem" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItem(jsondict)
        if "ExplanationOfBenefitItemAdjudication" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemAdjudication(jsondict)
        if "ExplanationOfBenefitItemDetail" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetail(jsondict)
        if "ExplanationOfBenefitItemDetailAdjudication" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetailAdjudication(jsondict)
        if "ExplanationOfBenefitItemDetailSubDetail" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail(jsondict)
        if "ExplanationOfBenefitItemDetailSubDetailAdjudication" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetailSubDetailAdjudication(jsondict)
        if "ExplanationOfBenefitItemProsthesis" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemProsthesis(jsondict)
        if "ExplanationOfBenefitMissingTeeth" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitMissingTeeth(jsondict)
        if "ExplanationOfBenefitNote" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitNote(jsondict)
        if "ExplanationOfBenefitPayee" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitPayee(jsondict)
        if "Extension" == resource_name:
            from . import extension
            return extension.Extension(jsondict)
        if "FamilyMemberHistory" == resource_name:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistory(jsondict)
        if "FamilyMemberHistoryCondition" == resource_name:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistoryCondition(jsondict)
        if "Flag" == resource_name:
            from . import flag
            return flag.Flag(jsondict)
        if "Goal" == resource_name:
            from . import goal
            return goal.Goal(jsondict)
        if "GoalOutcome" == resource_name:
            from . import goal
            return goal.GoalOutcome(jsondict)
        if "Group" == resource_name:
            from . import group
            return group.Group(jsondict)
        if "GroupCharacteristic" == resource_name:
            from . import group
            return group.GroupCharacteristic(jsondict)
        if "GroupMember" == resource_name:
            from . import group
            return group.GroupMember(jsondict)
        if "GuidanceResponse" == resource_name:
            from . import guidanceresponse
            return guidanceresponse.GuidanceResponse(jsondict)
        if "GuidanceResponseAction" == resource_name:
            from . import guidanceresponse
            return guidanceresponse.GuidanceResponseAction(jsondict)
        if "HealthcareService" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareService(jsondict)
        if "HealthcareServiceAvailableTime" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceAvailableTime(jsondict)
        if "HealthcareServiceNotAvailable" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailable(jsondict)
        if "HealthcareServiceServiceType" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceServiceType(jsondict)
        if "HumanName" == resource_name:
            from . import humanname
            return humanname.HumanName(jsondict)
        if "Identifier" == resource_name:
            from . import identifier
            return identifier.Identifier(jsondict)
        if "ImagingObjectSelection" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelection(jsondict)
        if "ImagingObjectSelectionStudy" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudy(jsondict)
        if "ImagingObjectSelectionStudySeries" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeries(jsondict)
        if "ImagingObjectSelectionStudySeriesInstance" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstance(jsondict)
        if "ImagingObjectSelectionStudySeriesInstanceFrame" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstanceFrame(jsondict)
        if "ImagingStudy" == resource_name:
            from . import imagingstudy
            return imagingstudy.ImagingStudy(jsondict)
        if "ImagingStudySeries" == resource_name:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeries(jsondict)
        if "ImagingStudySeriesInstance" == resource_name:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesInstance(jsondict)
        if "Immunization" == resource_name:
            from . import immunization
            return immunization.Immunization(jsondict)
        if "ImmunizationExplanation" == resource_name:
            from . import immunization
            return immunization.ImmunizationExplanation(jsondict)
        if "ImmunizationReaction" == resource_name:
            from . import immunization
            return immunization.ImmunizationReaction(jsondict)
        if "ImmunizationRecommendation" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendation" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(jsondict)
        if "ImmunizationRecommendationRecommendationProtocol" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationProtocol(jsondict)
        if "ImmunizationVaccinationProtocol" == resource_name:
            from . import immunization
            return immunization.ImmunizationVaccinationProtocol(jsondict)
        if "ImplementationGuide" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuide(jsondict)
        if "ImplementationGuideContact" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuideContact(jsondict)
        if "ImplementationGuideDependency" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuideDependency(jsondict)
        if "ImplementationGuideGlobal" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuideGlobal(jsondict)
        if "ImplementationGuidePackage" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuidePackage(jsondict)
        if "ImplementationGuidePackageResource" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuidePackageResource(jsondict)
        if "ImplementationGuidePage" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuidePage(jsondict)
        if "Library" == resource_name:
            from . import library
            return library.Library(jsondict)
        if "LibraryCodeSystem" == resource_name:
            from . import library
            return library.LibraryCodeSystem(jsondict)
        if "LibraryLibrary" == resource_name:
            from . import library
            return library.LibraryLibrary(jsondict)
        if "LibraryModel" == resource_name:
            from . import library
            return library.LibraryModel(jsondict)
        if "LibraryValueSet" == resource_name:
            from . import library
            return library.LibraryValueSet(jsondict)
        if "Linkage" == resource_name:
            from . import linkage
            return linkage.Linkage(jsondict)
        if "LinkageItem" == resource_name:
            from . import linkage
            return linkage.LinkageItem(jsondict)
        if "List" == resource_name:
            from . import list
            return list.List(jsondict)
        if "ListEntry" == resource_name:
            from . import list
            return list.ListEntry(jsondict)
        if "Location" == resource_name:
            from . import location
            return location.Location(jsondict)
        if "LocationPosition" == resource_name:
            from . import location
            return location.LocationPosition(jsondict)
        if "Measure" == resource_name:
            from . import measure
            return measure.Measure(jsondict)
        if "MeasureGroup" == resource_name:
            from . import measure
            return measure.MeasureGroup(jsondict)
        if "MeasureGroupPopulation" == resource_name:
            from . import measure
            return measure.MeasureGroupPopulation(jsondict)
        if "MeasureGroupStratifier" == resource_name:
            from . import measure
            return measure.MeasureGroupStratifier(jsondict)
        if "MeasureReport" == resource_name:
            from . import measurereport
            return measurereport.MeasureReport(jsondict)
        if "MeasureReportEvaluatedResources" == resource_name:
            from . import measurereport
            return measurereport.MeasureReportEvaluatedResources(jsondict)
        if "MeasureReportPopulationReport" == resource_name:
            from . import measurereport
            return measurereport.MeasureReportPopulationReport(jsondict)
        if "MeasureReportPopulationReportPopulation" == resource_name:
            from . import measurereport
            return measurereport.MeasureReportPopulationReportPopulation(jsondict)
        if "MeasureReportPopulationReportStratifier" == resource_name:
            from . import measurereport
            return measurereport.MeasureReportPopulationReportStratifier(jsondict)
        if "MeasureReportPopulationReportStratifierPopulation" == resource_name:
            from . import measurereport
            return measurereport.MeasureReportPopulationReportStratifierPopulation(jsondict)
        if "MeasureReportPopulationReportSupplementalData" == resource_name:
            from . import measurereport
            return measurereport.MeasureReportPopulationReportSupplementalData(jsondict)
        if "MeasureReportPopulationReportSupplementalDataStratifier" == resource_name:
            from . import measurereport
            return measurereport.MeasureReportPopulationReportSupplementalDataStratifier(jsondict)
        if "MeasureSupplementalData" == resource_name:
            from . import measure
            return measure.MeasureSupplementalData(jsondict)
        if "Media" == resource_name:
            from . import media
            return media.Media(jsondict)
        if "Medication" == resource_name:
            from . import medication
            return medication.Medication(jsondict)
        if "MedicationAdministration" == resource_name:
            from . import medicationadministration
            return medicationadministration.MedicationAdministration(jsondict)
        if "MedicationAdministrationDosage" == resource_name:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationDosage(jsondict)
        if "MedicationDispense" == resource_name:
            from . import medicationdispense
            return medicationdispense.MedicationDispense(jsondict)
        if "MedicationDispenseDosageInstruction" == resource_name:
            from . import medicationdispense
            return medicationdispense.MedicationDispenseDosageInstruction(jsondict)
        if "MedicationDispenseSubstitution" == resource_name:
            from . import medicationdispense
            return medicationdispense.MedicationDispenseSubstitution(jsondict)
        if "MedicationOrder" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrder(jsondict)
        if "MedicationOrderDispenseRequest" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrderDispenseRequest(jsondict)
        if "MedicationOrderDosageInstruction" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrderDosageInstruction(jsondict)
        if "MedicationOrderSubstitution" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrderSubstitution(jsondict)
        if "MedicationPackage" == resource_name:
            from . import medication
            return medication.MedicationPackage(jsondict)
        if "MedicationPackageContent" == resource_name:
            from . import medication
            return medication.MedicationPackageContent(jsondict)
        if "MedicationProduct" == resource_name:
            from . import medication
            return medication.MedicationProduct(jsondict)
        if "MedicationProductBatch" == resource_name:
            from . import medication
            return medication.MedicationProductBatch(jsondict)
        if "MedicationProductIngredient" == resource_name:
            from . import medication
            return medication.MedicationProductIngredient(jsondict)
        if "MedicationStatement" == resource_name:
            from . import medicationstatement
            return medicationstatement.MedicationStatement(jsondict)
        if "MedicationStatementDosage" == resource_name:
            from . import medicationstatement
            return medicationstatement.MedicationStatementDosage(jsondict)
        if "MessageHeader" == resource_name:
            from . import messageheader
            return messageheader.MessageHeader(jsondict)
        if "MessageHeaderDestination" == resource_name:
            from . import messageheader
            return messageheader.MessageHeaderDestination(jsondict)
        if "MessageHeaderResponse" == resource_name:
            from . import messageheader
            return messageheader.MessageHeaderResponse(jsondict)
        if "MessageHeaderSource" == resource_name:
            from . import messageheader
            return messageheader.MessageHeaderSource(jsondict)
        if "Meta" == resource_name:
            from . import meta
            return meta.Meta(jsondict)
        if "ModuleDefinition" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinition(jsondict)
        if "ModuleDefinitionCodeSystem" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionCodeSystem(jsondict)
        if "ModuleDefinitionData" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionData(jsondict)
        if "ModuleDefinitionDataCodeFilter" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionDataCodeFilter(jsondict)
        if "ModuleDefinitionDataDateFilter" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionDataDateFilter(jsondict)
        if "ModuleDefinitionLibrary" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionLibrary(jsondict)
        if "ModuleDefinitionModel" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionModel(jsondict)
        if "ModuleDefinitionParameter" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionParameter(jsondict)
        if "ModuleDefinitionValueSet" == resource_name:
            from . import moduledefinition
            return moduledefinition.ModuleDefinitionValueSet(jsondict)
        if "ModuleMetadata" == resource_name:
            from . import modulemetadata
            return modulemetadata.ModuleMetadata(jsondict)
        if "ModuleMetadataContact" == resource_name:
            from . import modulemetadata
            return modulemetadata.ModuleMetadataContact(jsondict)
        if "ModuleMetadataContributor" == resource_name:
            from . import modulemetadata
            return modulemetadata.ModuleMetadataContributor(jsondict)
        if "ModuleMetadataContributorContact" == resource_name:
            from . import modulemetadata
            return modulemetadata.ModuleMetadataContributorContact(jsondict)
        if "ModuleMetadataCoverage" == resource_name:
            from . import modulemetadata
            return modulemetadata.ModuleMetadataCoverage(jsondict)
        if "ModuleMetadataRelatedResource" == resource_name:
            from . import modulemetadata
            return modulemetadata.ModuleMetadataRelatedResource(jsondict)
        if "Money" == resource_name:
            from . import money
            return money.Money(jsondict)
        if "NamingSystem" == resource_name:
            from . import namingsystem
            return namingsystem.NamingSystem(jsondict)
        if "NamingSystemContact" == resource_name:
            from . import namingsystem
            return namingsystem.NamingSystemContact(jsondict)
        if "NamingSystemUniqueId" == resource_name:
            from . import namingsystem
            return namingsystem.NamingSystemUniqueId(jsondict)
        if "Narrative" == resource_name:
            from . import narrative
            return narrative.Narrative(jsondict)
        if "NutritionOrder" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrder(jsondict)
        if "NutritionOrderEnteralFormula" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormula(jsondict)
        if "NutritionOrderEnteralFormulaAdministration" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormulaAdministration(jsondict)
        if "NutritionOrderOralDiet" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDiet(jsondict)
        if "NutritionOrderOralDietNutrient" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietNutrient(jsondict)
        if "NutritionOrderOralDietTexture" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietTexture(jsondict)
        if "NutritionOrderSupplement" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderSupplement(jsondict)
        if "Observation" == resource_name:
            from . import observation
            return observation.Observation(jsondict)
        if "ObservationComponent" == resource_name:
            from . import observation
            return observation.ObservationComponent(jsondict)
        if "ObservationReferenceRange" == resource_name:
            from . import observation
            return observation.ObservationReferenceRange(jsondict)
        if "ObservationRelated" == resource_name:
            from . import observation
            return observation.ObservationRelated(jsondict)
        if "OperationDefinition" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinition(jsondict)
        if "OperationDefinitionContact" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionContact(jsondict)
        if "OperationDefinitionParameter" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameter(jsondict)
        if "OperationDefinitionParameterBinding" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterBinding(jsondict)
        if "OperationOutcome" == resource_name:
            from . import operationoutcome
            return operationoutcome.OperationOutcome(jsondict)
        if "OperationOutcomeIssue" == resource_name:
            from . import operationoutcome
            return operationoutcome.OperationOutcomeIssue(jsondict)
        if "Order" == resource_name:
            from . import order
            return order.Order(jsondict)
        if "OrderResponse" == resource_name:
            from . import orderresponse
            return orderresponse.OrderResponse(jsondict)
        if "OrderSet" == resource_name:
            from . import orderset
            return orderset.OrderSet(jsondict)
        if "OrderWhen" == resource_name:
            from . import order
            return order.OrderWhen(jsondict)
        if "Organization" == resource_name:
            from . import organization
            return organization.Organization(jsondict)
        if "OrganizationContact" == resource_name:
            from . import organization
            return organization.OrganizationContact(jsondict)
        if "ParameterDefinition" == resource_name:
            from . import parameterdefinition
            return parameterdefinition.ParameterDefinition(jsondict)
        if "Parameters" == resource_name:
            from . import parameters
            return parameters.Parameters(jsondict)
        if "ParametersParameter" == resource_name:
            from . import parameters
            return parameters.ParametersParameter(jsondict)
        if "Patient" == resource_name:
            from . import patient
            return patient.Patient(jsondict)
        if "PatientAnimal" == resource_name:
            from . import patient
            return patient.PatientAnimal(jsondict)
        if "PatientCommunication" == resource_name:
            from . import patient
            return patient.PatientCommunication(jsondict)
        if "PatientContact" == resource_name:
            from . import patient
            return patient.PatientContact(jsondict)
        if "PatientLink" == resource_name:
            from . import patient
            return patient.PatientLink(jsondict)
        if "PaymentNotice" == resource_name:
            from . import paymentnotice
            return paymentnotice.PaymentNotice(jsondict)
        if "PaymentReconciliation" == resource_name:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliation(jsondict)
        if "PaymentReconciliationDetail" == resource_name:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationDetail(jsondict)
        if "PaymentReconciliationNote" == resource_name:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationNote(jsondict)
        if "Period" == resource_name:
            from . import period
            return period.Period(jsondict)
        if "Person" == resource_name:
            from . import person
            return person.Person(jsondict)
        if "PersonLink" == resource_name:
            from . import person
            return person.PersonLink(jsondict)
        if "Practitioner" == resource_name:
            from . import practitioner
            return practitioner.Practitioner(jsondict)
        if "PractitionerPractitionerRole" == resource_name:
            from . import practitioner
            return practitioner.PractitionerPractitionerRole(jsondict)
        if "PractitionerQualification" == resource_name:
            from . import practitioner
            return practitioner.PractitionerQualification(jsondict)
        if "Procedure" == resource_name:
            from . import procedure
            return procedure.Procedure(jsondict)
        if "ProcedureFocalDevice" == resource_name:
            from . import procedure
            return procedure.ProcedureFocalDevice(jsondict)
        if "ProcedurePerformer" == resource_name:
            from . import procedure
            return procedure.ProcedurePerformer(jsondict)
        if "ProcedureRequest" == resource_name:
            from . import procedurerequest
            return procedurerequest.ProcedureRequest(jsondict)
        if "ProcessRequest" == resource_name:
            from . import processrequest
            return processrequest.ProcessRequest(jsondict)
        if "ProcessRequestItem" == resource_name:
            from . import processrequest
            return processrequest.ProcessRequestItem(jsondict)
        if "ProcessResponse" == resource_name:
            from . import processresponse
            return processresponse.ProcessResponse(jsondict)
        if "ProcessResponseNotes" == resource_name:
            from . import processresponse
            return processresponse.ProcessResponseNotes(jsondict)
        if "Protocol" == resource_name:
            from . import protocol
            return protocol.Protocol(jsondict)
        if "ProtocolStep" == resource_name:
            from . import protocol
            return protocol.ProtocolStep(jsondict)
        if "ProtocolStepActivity" == resource_name:
            from . import protocol
            return protocol.ProtocolStepActivity(jsondict)
        if "ProtocolStepActivityComponent" == resource_name:
            from . import protocol
            return protocol.ProtocolStepActivityComponent(jsondict)
        if "ProtocolStepActivityDetail" == resource_name:
            from . import protocol
            return protocol.ProtocolStepActivityDetail(jsondict)
        if "ProtocolStepNext" == resource_name:
            from . import protocol
            return protocol.ProtocolStepNext(jsondict)
        if "ProtocolStepPrecondition" == resource_name:
            from . import protocol
            return protocol.ProtocolStepPrecondition(jsondict)
        if "ProtocolStepPreconditionCondition" == resource_name:
            from . import protocol
            return protocol.ProtocolStepPreconditionCondition(jsondict)
        if "Provenance" == resource_name:
            from . import provenance
            return provenance.Provenance(jsondict)
        if "ProvenanceAgent" == resource_name:
            from . import provenance
            return provenance.ProvenanceAgent(jsondict)
        if "ProvenanceAgentRelatedAgent" == resource_name:
            from . import provenance
            return provenance.ProvenanceAgentRelatedAgent(jsondict)
        if "ProvenanceEntity" == resource_name:
            from . import provenance
            return provenance.ProvenanceEntity(jsondict)
        if "Quantity" == resource_name:
            from . import quantity
            return quantity.Quantity(jsondict)
        if "Questionnaire" == resource_name:
            from . import questionnaire
            return questionnaire.Questionnaire(jsondict)
        if "QuestionnaireItem" == resource_name:
            from . import questionnaire
            return questionnaire.QuestionnaireItem(jsondict)
        if "QuestionnaireResponse" == resource_name:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponse(jsondict)
        if "QuestionnaireResponseItem" == resource_name:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItem(jsondict)
        if "QuestionnaireResponseItemAnswer" == resource_name:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItemAnswer(jsondict)
        if "Range" == resource_name:
            from . import range
            return range.Range(jsondict)
        if "Ratio" == resource_name:
            from . import ratio
            return ratio.Ratio(jsondict)
        if "Reference" == resource_name:
            from . import reference
            return reference.Reference(jsondict)
        if "ReferralRequest" == resource_name:
            from . import referralrequest
            return referralrequest.ReferralRequest(jsondict)
        if "RelatedPerson" == resource_name:
            from . import relatedperson
            return relatedperson.RelatedPerson(jsondict)
        if "Resource" == resource_name:
            from . import resource
            return resource.Resource(jsondict)
        if "RiskAssessment" == resource_name:
            from . import riskassessment
            return riskassessment.RiskAssessment(jsondict)
        if "RiskAssessmentPrediction" == resource_name:
            from . import riskassessment
            return riskassessment.RiskAssessmentPrediction(jsondict)
        if "SampledData" == resource_name:
            from . import sampleddata
            return sampleddata.SampledData(jsondict)
        if "Schedule" == resource_name:
            from . import schedule
            return schedule.Schedule(jsondict)
        if "SearchParameter" == resource_name:
            from . import searchparameter
            return searchparameter.SearchParameter(jsondict)
        if "SearchParameterContact" == resource_name:
            from . import searchparameter
            return searchparameter.SearchParameterContact(jsondict)
        if "Sequence" == resource_name:
            from . import sequence
            return sequence.Sequence(jsondict)
        if "SequenceChip" == resource_name:
            from . import sequence
            return sequence.SequenceChip(jsondict)
        if "SequenceCoordinate" == resource_name:
            from . import sequence
            return sequence.SequenceCoordinate(jsondict)
        if "SequenceQuality" == resource_name:
            from . import sequence
            return sequence.SequenceQuality(jsondict)
        if "SequenceRepository" == resource_name:
            from . import sequence
            return sequence.SequenceRepository(jsondict)
        if "Signature" == resource_name:
            from . import signature
            return signature.Signature(jsondict)
        if "Slot" == resource_name:
            from . import slot
            return slot.Slot(jsondict)
        if "Specimen" == resource_name:
            from . import specimen
            return specimen.Specimen(jsondict)
        if "SpecimenCollection" == resource_name:
            from . import specimen
            return specimen.SpecimenCollection(jsondict)
        if "SpecimenContainer" == resource_name:
            from . import specimen
            return specimen.SpecimenContainer(jsondict)
        if "SpecimenTreatment" == resource_name:
            from . import specimen
            return specimen.SpecimenTreatment(jsondict)
        if "StructureDefinition" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinition(jsondict)
        if "StructureDefinitionContact" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionContact(jsondict)
        if "StructureDefinitionDifferential" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionDifferential(jsondict)
        if "StructureDefinitionMapping" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionMapping(jsondict)
        if "StructureDefinitionSnapshot" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionSnapshot(jsondict)
        if "StructureMap" == resource_name:
            from . import structuremap
            return structuremap.StructureMap(jsondict)
        if "StructureMapContact" == resource_name:
            from . import structuremap
            return structuremap.StructureMapContact(jsondict)
        if "StructureMapGroup" == resource_name:
            from . import structuremap
            return structuremap.StructureMapGroup(jsondict)
        if "StructureMapGroupInput" == resource_name:
            from . import structuremap
            return structuremap.StructureMapGroupInput(jsondict)
        if "StructureMapGroupRule" == resource_name:
            from . import structuremap
            return structuremap.StructureMapGroupRule(jsondict)
        if "StructureMapGroupRuleDependent" == resource_name:
            from . import structuremap
            return structuremap.StructureMapGroupRuleDependent(jsondict)
        if "StructureMapGroupRuleSource" == resource_name:
            from . import structuremap
            return structuremap.StructureMapGroupRuleSource(jsondict)
        if "StructureMapGroupRuleTarget" == resource_name:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTarget(jsondict)
        if "StructureMapGroupRuleTargetParameter" == resource_name:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTargetParameter(jsondict)
        if "StructureMapStructure" == resource_name:
            from . import structuremap
            return structuremap.StructureMapStructure(jsondict)
        if "Subscription" == resource_name:
            from . import subscription
            return subscription.Subscription(jsondict)
        if "SubscriptionChannel" == resource_name:
            from . import subscription
            return subscription.SubscriptionChannel(jsondict)
        if "Substance" == resource_name:
            from . import substance
            return substance.Substance(jsondict)
        if "SubstanceIngredient" == resource_name:
            from . import substance
            return substance.SubstanceIngredient(jsondict)
        if "SubstanceInstance" == resource_name:
            from . import substance
            return substance.SubstanceInstance(jsondict)
        if "SupplyDelivery" == resource_name:
            from . import supplydelivery
            return supplydelivery.SupplyDelivery(jsondict)
        if "SupplyRequest" == resource_name:
            from . import supplyrequest
            return supplyrequest.SupplyRequest(jsondict)
        if "SupplyRequestWhen" == resource_name:
            from . import supplyrequest
            return supplyrequest.SupplyRequestWhen(jsondict)
        if "Task" == resource_name:
            from . import task
            return task.Task(jsondict)
        if "TaskInput" == resource_name:
            from . import task
            return task.TaskInput(jsondict)
        if "TaskOutput" == resource_name:
            from . import task
            return task.TaskOutput(jsondict)
        if "TestScript" == resource_name:
            from . import testscript
            return testscript.TestScript(jsondict)
        if "TestScriptContact" == resource_name:
            from . import testscript
            return testscript.TestScriptContact(jsondict)
        if "TestScriptDestination" == resource_name:
            from . import testscript
            return testscript.TestScriptDestination(jsondict)
        if "TestScriptFixture" == resource_name:
            from . import testscript
            return testscript.TestScriptFixture(jsondict)
        if "TestScriptMetadata" == resource_name:
            from . import testscript
            return testscript.TestScriptMetadata(jsondict)
        if "TestScriptMetadataCapability" == resource_name:
            from . import testscript
            return testscript.TestScriptMetadataCapability(jsondict)
        if "TestScriptMetadataLink" == resource_name:
            from . import testscript
            return testscript.TestScriptMetadataLink(jsondict)
        if "TestScriptOrigin" == resource_name:
            from . import testscript
            return testscript.TestScriptOrigin(jsondict)
        if "TestScriptSetup" == resource_name:
            from . import testscript
            return testscript.TestScriptSetup(jsondict)
        if "TestScriptSetupAction" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupAction(jsondict)
        if "TestScriptSetupActionAssert" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupActionAssert(jsondict)
        if "TestScriptSetupActionOperation" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupActionOperation(jsondict)
        if "TestScriptSetupActionOperationRequestHeader" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupActionOperationRequestHeader(jsondict)
        if "TestScriptTeardown" == resource_name:
            from . import testscript
            return testscript.TestScriptTeardown(jsondict)
        if "TestScriptTeardownAction" == resource_name:
            from . import testscript
            return testscript.TestScriptTeardownAction(jsondict)
        if "TestScriptTest" == resource_name:
            from . import testscript
            return testscript.TestScriptTest(jsondict)
        if "TestScriptTestAction" == resource_name:
            from . import testscript
            return testscript.TestScriptTestAction(jsondict)
        if "TestScriptVariable" == resource_name:
            from . import testscript
            return testscript.TestScriptVariable(jsondict)
        if "Timing" == resource_name:
            from . import timing
            return timing.Timing(jsondict)
        if "TimingRepeat" == resource_name:
            from . import timing
            return timing.TimingRepeat(jsondict)
        if "TriggerDefinition" == resource_name:
            from . import triggerdefinition
            return triggerdefinition.TriggerDefinition(jsondict)
        if "ValueSet" == resource_name:
            from . import valueset
            return valueset.ValueSet(jsondict)
        if "ValueSetCompose" == resource_name:
            from . import valueset
            return valueset.ValueSetCompose(jsondict)
        if "ValueSetComposeInclude" == resource_name:
            from . import valueset
            return valueset.ValueSetComposeInclude(jsondict)
        if "ValueSetComposeIncludeConcept" == resource_name:
            from . import valueset
            return valueset.ValueSetComposeIncludeConcept(jsondict)
        if "ValueSetComposeIncludeConceptDesignation" == resource_name:
            from . import valueset
            return valueset.ValueSetComposeIncludeConceptDesignation(jsondict)
        if "ValueSetComposeIncludeFilter" == resource_name:
            from . import valueset
            return valueset.ValueSetComposeIncludeFilter(jsondict)
        if "ValueSetContact" == resource_name:
            from . import valueset
            return valueset.ValueSetContact(jsondict)
        if "ValueSetExpansion" == resource_name:
            from . import valueset
            return valueset.ValueSetExpansion(jsondict)
        if "ValueSetExpansionContains" == resource_name:
            from . import valueset
            return valueset.ValueSetExpansionContains(jsondict)
        if "ValueSetExpansionParameter" == resource_name:
            from . import valueset
            return valueset.ValueSetExpansionParameter(jsondict)
        if "VisionPrescription" == resource_name:
            from . import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        if "VisionPrescriptionDispense" == resource_name:
            from . import visionprescription
            return visionprescription.VisionPrescriptionDispense(jsondict)
        return element.Element(json)
