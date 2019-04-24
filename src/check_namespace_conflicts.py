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
This program runs through all concepts and marks whether they are in the US-GAAP, DEI or SOLAR
namespaces.  It will print warnings for any concepts that are not in any of the namespaces
and also list any concepts that are present in both namespaces.
"""

from oblib import taxonomy

tax = taxonomy.Taxonomy()
concepts = {}

entrypoints = tax.semantic.get_all_entrypoints()
for entrypoint in entrypoints:
    cc = tax.semantic.get_entrypoint_concepts(entrypoint)
    for c in cc:
        parts = c.split(":")
        if parts[1] in concepts:
            namespaces = concepts[parts[1]]
            if parts[0] == "us-gaap":
                namespaces[0] = True
            elif parts[0] == "solar":
                namespaces[1] = True
            elif parts[0] == "dei":
                namespaces[2] = True
            else:
                print("Warning, alternative namespace found ", c)
        else:
            namespaces = [False, False, False]
            if parts[0] == "us-gaap":
                namespaces[0] = True
            elif parts[0] == "solar":
                namespaces[1] = True
            elif parts[0] == "dei":
                namespaces[2] = True
            else:
                print("Warning, alternative namespace found ", c)
            concepts[parts[1]] = namespaces

print("List of namespace conflicts")
print("===========================")
for concept in concepts:
    namespace = concepts[concept]
    if (namespace[0] and namespace[1]) or (namespace[0] and namespace[2]) or (namespace[1] and namespace[2]):
        print(concept, concepts[concept])
print()