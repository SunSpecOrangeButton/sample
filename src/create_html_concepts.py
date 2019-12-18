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
This HTML viewpoints of Orange Button Entrypoints.

NOTE: This is in a very early and experimental mode.  Reading the relationships
is somewhat trial and error and needs extensive update.  Github is being primarily
used as Backup at this point and this is in no way ready for general usage.
"""

from oblib import taxonomy

import re
import sys

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)

TYPES = {    
    "dei:legalEntityIdentifierItemType": "String",
    "nonnum:domainItemType": "String",
    "num-us:electricCurrentItemType":  "Float",
    "num-us:frequencyItemType": "Float",
    "num-us:insolationItemType": "Float",
    "num-us:irradianceItemType": "Float",
    "num-us:planeAngleItemType": "Float",
    "num-us:pressureItemType": "Float",
    "num-us:speedItemType": "Float",
    "num-us:temperatureItemType": "Float",
    "num-us:voltageItemType": "Float",
    "num:areaItemType": "Float",
    "num:energyItemType": "Float",
    "num:lengthItemType": "Float",
    "num:massItemType": "Float",
    "num:percentItemType": "Float",
    "num:powerItemType": "Float",
    "num:volumeItemType": "Float",
    "solar-types:DERItemType": "Enumeration",
    "solar-types:aLTASurveyItemType": "Enumeration",
    "solar-types:approvalRequestItemType": "Enumeration",
    "solar-types:approvalStatusItemType": "Enumeration",
    "solar-types:assetSecuredItemType": "Enumeration",
    "solar-types:batteryChemistryItemType": "Enumeration",
    "solar-types:batteryConnectionItemType": "Enumeration",
    "solar-types:climateClassificationKoppenItemType": "Enumeration",
    "solar-types:climateZoneANSIItemType": "Enumeration",
    "solar-types:communicationProtocolItemType": "Enumeration",
    "solar-types:creditSupportStatusItemType": "Enumeration",
    "solar-types:deviceItemType": "Enumeration",
    "solar-types:distributedGenOrUtilityScaleItemType": "Enumeration",
    "solar-types:divisionStateApprovalStatusItemType": "Enumeration",
    "solar-types:employeeLevelItemType": "Enumeration",
    "solar-types:employeeRoleItemType": "Enumeration",
    "solar-types:energyBudgetPhaseItemType": "Enumeration",
    "solar-types:eventSeverityItemType": "Enumeration",
    "solar-types:eventStatusItemType": "Enumeration",
    "solar-types:feeStatusItemType": "Enumeration",
    "solar-types:financialTransactionItemType": "Enumeration",
    "solar-types:financingEventItemType": "Enumeration",
    "solar-types:fundOrProjectItemType": "Enumeration",
    "solar-types:fundStatusItemType": "Enumeration",
    "solar-types:gISFileFormatItemType": "Enumeration",
    "solar-types:hedgeItemType": "Enumeration",
    "solar-types:insuranceItemType": "Enumeration",
    "solar-types:internetConnectionItemType": "Enumeration",
    "solar-types:inverterItemType": "Enumeration",
    "solar-types:inverterPhaseItemType": "Enumeration",
    "solar-types:investmentStatusItemType": "Enumeration",
    "solar-types:mORLevelItemType": "Enumeration",
    "solar-types:moduleItemType": "Enumeration",
    "solar-types:moduleOrientationItemType": "Enumeration",
    "solar-types:moduleTechnologyItemType": "Enumeration",
    "solar-types:mountingItemType": "Enumeration",
    "solar-types:occupancyItemType": "Enumeration",
    "solar-types:optimizerTypeItemType": "Enumeration",
    "solar-types:participantItemType": "Enumeration",
    "solar-types:preventiveMaintenanceTaskStatusItemType": "Enumeration",
    "solar-types:projectAssetTypeItemType": "Enumeration",
    "solar-types:projectClassItemType": "Enumeration",
    "solar-types:projectInterconnectionItemType": "Enumeration",
    "solar-types:projectPhaseItemType": "Enumeration",
    "solar-types:projectStageItemType": "Enumeration",
    "solar-types:regulatoryApprovalStatusItemType": "Enumeration",
    "solar-types:regulatoryFacilityItemType": "Enumeration",
    "solar-types:reserveCollateralItemType": "Enumeration",
    "solar-types:reserveUseItemType": "Enumeration",
    "solar-types:roofItemType": "Enumeration",
    "solar-types:roofSlopeItemType": "Enumeration",
    "solar-types:securityInterestItemType": "Enumeration",
    "solar-types:securityInterestStatusItemType": "Enumeration",
    "solar-types:siteControlItemType": "Enumeration",
    "solar-types:solarSystemCharacterItemType": "Enumeration",
    "solar-types:sparePartsStatusItemType": "Enumeration",
    "solar-types:sPVOrCounterpartyItemType": "Enumeration",
    "solar-types:systemAvailabilityModeItemType": "Enumeration",
    "solar-types:systemOperationalStatusItemType": "Enumeration",
    "solar-types:titlePolicyInsuranceItemType": "Enumeration",
    "solar-types:trackerItemType": "Enumeration",
    "solar-types:uuidItemType": "String",
    "solar-types:uuidXbrlItemType": "String",
    "solar-types:zoningPermitPropertyItemType": "Enumeration",
    "us-types:perUnitItemType": "String",
    "xbrli:anyURIItemType": "URI",
    "xbrli:booleanItemType": "Boolean",
    "xbrli:dateItemType": "Date",
    "xbrli:decimalItemType": "Float",
    "xbrli:durationItemType": "String",
    "xbrli:integerItemType": "Integer",
    "xbrli:monetaryItemType": "Float",
    "xbrli:normalizedStringItemType": "String",
    "xbrli:pureItemType": "String",
    "xbrli:stringItemType": "String"

}


tax = taxonomy.Taxonomy()

if len(sys.argv) != 2:
    print("Incorrect number of arguments - 1 required")
    print("  Path to Output directory (example: ./somepath/outdir)")
    sys.exit(1)

with open(sys.argv[1] + "/" + "concepts.html", "w") as out:
    out.write("<html>\n")
    out.write("  <body>\n")
    out.write("     <h1>Concepts</h1>\n")

    for concept in tax.semantic.get_all_concepts(details=True):
        details = tax.semantic.get_concept_details(concept)
        if not details.abstract:
            out.write("      <h2>" + concept.replace("dei:", "").replace("us-gaap:", "").replace("solar:", "") + "</h2>\n")
            out.write("      <ul>\n")

            out.write("        <li>Label: " + convert(details.name) + "</li>\n")

            t = "SOLAR"
            if details.id.startswith("us-gaap:"):
                t = "US-GAAP"
            elif details.id.startswith("dei:"):
                t = "DEI"
            out.write("        <li>Taxonomy: " + t + "</li>\n")

            out.write("        <li>Entrypoints: \n")
            for entrypoint in tax.semantic.get_all_entrypoints():
                if entrypoint != "All":
                    if concept in tax.semantic.get_entrypoint_concepts(entrypoint):
                        out.write("        <ul>\n")
                        out.write("          <li>" + entrypoint + "</li>\n")
                        out.write("        </ul>\n")

            docs = tax.documentation.get_concept_documentation(concept)
            if docs is None:
                docs = "None"
            out.write("        <li>Description:</li>\n")
            out.write("        <ul>\n")
            out.write("          <li>" + docs + "</li>\n")
            out.write("        </ul>\n")
            out.write("        <br>\n")

            out.write("        <li>Item Type: " + details.type_name.split(":")[1].replace("ItemType", "") + "</li>\n")

            validation_rule = "None"
            t = TYPES[details.type_name]
            if t == "String":
                validation_rule = "Any String is valid"
            elif t == "Boolean":
                validation_rule = "Boolean values (TRUE or FALSE) are valid"
            elif t == "Integer":
                validation_rule = "Integer values (no decimal point) are valid"
            elif t == "Float":
                validation_rule = "Float values (with or without decimal point) are valid"
            elif t == "Enumeration":
                validation_rule = "Value must be one of the enumerated values listed below:"
            elif t == "URI":
                validation_rule = "Value must be a valid internet URI/URL format (but does not necessarily need to exist on the internet)"
            elif t == "UUID":
                validation_rule = "Value must be a valid UUID (xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx)"
            elif t == "LEI":
                validation_rule = "Value must be a 20 character LEI string"
            out.write("        <li>Validation Rule: " + validation_rule + "</li>\n")

            if t == "Enumeration":
                out.write("        <ul>\n")
                for e in tax.types.get_type_enum(details.type_name):
                    out.write("          <li>" + e + "</li>\n")
                out.write("        </ul>\n")

            if details.type_name.startswith("num:") or details.type_name.startswith("num-us:"):
                out.write("        <li>Precision/Decimals: Either Precision or Decimals must be specified</li>\n")
            else:
                out.write("        <li>Precision/Decimals: N/A (neither precision nor decimals may be specified)</li>\n")

            if details.type_name.startswith("num:") or details.type_name.startswith("num-us:"):
                out.write("        <li>Units:</li>\n")
                out.write("        <ul>\n")

                if details.type_name in ["num:percentItemType"]:
                    out.write("           <li>pure</li>\n")
                else:
                    for unit in tax.units.get_all_units():
                        ud = tax.units.get_unit(unit)
                        if details.type_name.lower().find(ud.item_type.lower()) != -1:
                            out.write("           <li>" + ud.unit_name + " </li>\n")

                out.write("        </ul>\n")
            else:
                out.write("        <li>Units: N/A (units may not be specified)</li>\n")

            period = details.period_type.value
            if period == "instant":
                period = "Instant in time"
            else:
                period = "Period of time"
            out.write("        <li>Period: " + period + "</li>\n")
            out.write("        <li>Nillable: " + str(details.nillable) + "</li>\n")

            if concept == "us-gaap:Revenues":
                calc = "Other Income + RebateRevenue + PeformanceBasedIncentiveRevenue + Electrical Generation Revenue = Revenues"
            else:
                calc = "N/A"
            out.write("        <li>Calculations: " + calc + "</li>\n")
            out.write("</li>\n")
            out.write("      </ul>\n")
    out.write("  </body>\n")
    out.write("</html>\n")