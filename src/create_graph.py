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
This program creates a DOT file for an entry point.  More information on DOT is
available at http://www.graphviz.org/.
"""

import sys

from oblib import taxonomy

if len(sys.argv) != 2:
    print("Program requires the name of an Entry Point")
    sys.exit()

tax = taxonomy.Taxonomy()

relationships = tax.semantic.get_entrypoint_relationships(sys.argv[1])
if relationships is None:
    print("Entry Point command line argument does not exist in Taxonomy.")
    sys.exit()

print("digraph G {")
if relationships is not None:
    for r in relationships:
        print('    %s -> %s;' %
                ( r.from_.split(":")[1], r.to.split(":")[1]))
print("}")
