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
This program searches for special characters in the Taxonomy.
"""


from oblib import taxonomy
import re

regex1 = re.compile('[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_ ]')
regex2 = re.compile('^[1234567890]')

tax = taxonomy.Taxonomy()

print("Types:")
print()

for type_ in tax.types.get_all_types():
    for e in tax.types.get_type_enum(type_):
        if regex1.search(e) != None or regex2.search(e) != None:
            print(type_, e)

print()
print("Units:")
print()

for unit in tax.units.get_all_units():
    if regex1.search(unit) != None or regex2.search(unit) != None:
        print(unit)

print()
print("Numeric Types:")
print()

for num_type in tax.numeric_types.get_all_numeric_types():
    num_type = num_type.replace("num-us:", "")
    if regex1.search(num_type) != None or regex2.search(num_type) != None:
        print(num_type)

print()
print("Ref Parts:")
print()

for ref_part in tax.ref_parts.get_all_ref_parts():
    if regex1.search(ref_part) != None or regex2.search(ref_part) != None:
        print(ref_part)

print()
print("Concepts:")
print()

cl = set()
for entrypoint in tax.semantic.get_all_entrypoints():
    for concept in tax.semantic.get_all_concepts(entrypoint):
        concept = concept.split(":")[1]
        if regex1.search(concept) != None or regex2.search(concept) != None:
            cl.add(concept)
for c in cl:
    print(c)