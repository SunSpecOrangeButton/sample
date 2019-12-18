# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This sample program creates a XBRL JSON Power Purchase Agreement populated with fake data.
It can be used as a starting point for building a program to create real Power Purchase Agreement
Orange Button data.
"""

from oblib import taxonomy, data_model, parser

import datetime

# Initialize oblib and create an Entrypoint for a Power Purchase Agreement
tax = taxonomy.Taxonomy()
ob_parser = parser.Parser(tax)
entrypoint = data_model.OBInstance("PowerPurchaseAgreement", tax, dev_validation_off=True)

#
# PowerPurcahseAgreements (PPA's) have two tables, a PowerPurchaseAgremeentContract table and an EnergyRateTable.
# Both tables can be placed in the same set of XBRL JSON (or XML).  They are both included in the code.
#

# Create 5 rows of data in the PowerPurchaseAgreementContract table
for i in range(0, 5):

    # The priamry key will be numbered 1-5 in each row, in a real application it can be set to any string value.
    pk_value = str(i+1)

    # Most of the elements require the primary key (called an Axis in XBRL terminology) and have a duration of forever.
    # A kwargs value is created which can be applied to this set of elements.
    kwargs = {}
    kwargs["duration"] = "forever"
    kwargs["solar:PowerPurchaseAgreementContractAxis"] = pk_value

    # Some entities require a instant in time (or date) to be set instead of a duration of forever.  Create another
    # kwargs value with the same PK and set the time to right now.  For a real application use the actual date instead.
    kwargs2 = {}
    kwargs2["instant"] = datetime.time()
    kwargs2["solar:PowerPurchaseAgreementContractAxis"] = pk_value

    # Now set all of the Concepts (columns in the table) to a Sample Value.  Replace with real values in an actual
    # application.  Apply kwargs or kwargs2 as appropriate.
    entrypoint.set("solar:DocumentIdentifierPowerPurchaseAgreement", "Sample String", **kwargs)
    entrypoint.set("solar:PreparerOfPowerPurchaseAgreement", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementDescription", "Sample String", **kwargs)
    entrypoint.set("solar:SystemCommercialOperationsDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:SystemExpectedCommercialOperationsDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsOriginalTermOfPowerPurchaseAgreementLease", "UNKNOWN", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsDateOfContractInitiation", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsDateOfContractExpiration", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPaymentFrequency", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsAssignmentProvisions", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsBuyoutOptionsinPPA", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsCommercialOperationsDateGuaranty", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsContractHistoryAndStructure", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsCurtailmentProvisions", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsDefaultProvisions", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsEffectiveDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsEndofTermProvisions", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsFinancialAssurances", "Sample String", **kwargs)
    entrypoint.set("solar:OffTakerIdentifier", "Sample String", **kwargs)
    entrypoint.set("solar:OffTakerName", "Sample String", **kwargs)
    entrypoint.set("solar:OfftakerEmail", "Sample String", **kwargs)
    entrypoint.set("solar:SiteLongitudeAtRevenueMeter", 33.33, **kwargs)
    entrypoint.set("solar:SiteLatitudeAtRevenueMeter", 33.33, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsProductionGuarantee", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsProvider", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsSpecialCustomerRightsAndObligations", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsSpecialFeatures", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsSpecialProviderRightsAndObligations", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPATerm", "UNKNOWN", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractAdditionalTermNumber", 99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractAdditionalTermDuration", "UNKNOWN", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementPurchaserOptionToPurchase", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsTerminationRights", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsTransmissionAndSchedulingResponsibilities", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsSiteLeaseAgreement", True, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsLimitationofLiability", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsInsuranceRequirements", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPowerOfftakeAgreementType", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAAmendmentExecutionDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAAmendmentEffectiveDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAAmendmentExpirationDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPACounterparty", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAFirmVolume", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAGuaranteedOutput", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAPerformanceGuarantee", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAPerformanceGuaranteeTerm", "UNKNOWN", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAPerformanceGuaranteeType", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAPerformanceGuaranteeExpirationDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAPerformanceGuaranteeInitiationDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsRenewableEnergyCreditsBundledWithElectricity", 9999.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateEscalator", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateType", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateTimeOfUseFlag", True, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateProductionCap", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateProductionGuarantee", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateProductionGuaranteeTiming", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateSystemTrueUpProduction", 99.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateTrueupTiming", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateLongTermContractForPurchaseOfElectricPowerDateOfContractExpiration", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateSeasoningNumberOfPaymentsMade", 99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateTotalUpfrontPayment", 9999.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateAmountActualToInception", 9999.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateCounterpartyReportingRequirements", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateCounterpartyTaxObligationsDescription", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateExpectedAmount", 9999.99, **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateAddressForInvoices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateNameOfContactToSendInvoices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateCompanyInvoicesSentTo", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateEmailAddressToSendInvoices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRatePhoneOfInvoicesContact", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateInvoicingDate", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateContactAddressToReceiveNotices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateContactToReceiveNotices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateContactEmailToReceiveNotices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateNameOfHostToReceiveNotices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRateHostTelephoneToReceiveNotices", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRatePaymentDeadline", "2018-01-02", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementRatePaymentMethod", "Sample String", **kwargs)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAPortionOfSite", 99.99, **kwargs2)
    entrypoint.set("solar:PowerPurchaseAgreementContractTermsPPAPortionoFUnits", 99, **kwargs2)
    entrypoint.set("solar:PowerPurchaseAgreementRateRemainingTermofPowerPurchaseAgreementLease", "UNKNOWN", **kwargs2)
    entrypoint.set("solar:PowerPurchaseAgreementRateActualAmount", 9999.99, **kwargs2)
    entrypoint.set("solar:PowerPurchaseAgreementRateCounterpartyTaxObligationsAmount", 9999.99, **kwargs2)
    entrypoint.set("solar:PowerPurchaseAgreementRateExpectedAmountInceptionToDate", 9999.99, **kwargs2)

#
# Create the Energy Rate table.  There are four PK values (Axis's) in the EnergyRate table and a single
# unit (EnergyContractRatePricePerEnergyUnit) whic will always be set to 45.45 in our example.
#
# The PK's are as follows:
#    MonthlyPeriodAxis: Set to a Month following this sample format: "PeriodMonthMarchMember"
#    EnergyContractHourlyRateAxis: Set to a Hour following this sample format: "EnergyContractHourlyRate3Member"
#    PowerPurcahseAgreementContractAxis: User defined (will be set to 1 in our example)
#    EnergyContractyearlyRateAxis: User defined (will be set to 1 in our example)
#

# Loop through Months and Hours in the day
for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    for hour in range(0, 24):
        kwargs = {}
        kwargs["duration"] = "forever"
        kwargs["solar:MonthlyPeriodAxis"] = "solar:PeriodMonth" + month + "Member"
        kwargs["solar:EnergyContractHourlyRateAxis"] = "solar:EnergyContractHourlyRateHour" + str(hour+1) +"Member"
        kwargs["solar:PowerPurchaseAgreementContractAxis"] = 1
        kwargs["solar:EnergyContractYearlyRateAxis"] = 1
        entrypoint.set("solar:EnergyContractRatePricePerEnergyUnit", 45.45, **kwargs)

# Now create JSON and print it.  Note taht there are other methods taht could be used:
#
#   ob_parser.to_JSON(filename) - places output in a file instead of a string
#   ob_parser.to_XML_string() - creates XML instead of JSON
#   ob_parser.to_XML(filename) = creates XML and places output in a file instead of a string
json = ob_parser.to_JSON_string(entrypoint)
print(json)
