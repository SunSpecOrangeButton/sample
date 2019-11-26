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

import sys


def header(out):
    out.write("<html>\n")
    out.write("  <body>\n")


def abstract(out, abstract, level):
    if level == 1:
        out.write("    <h1>" + abstract + "</h1>\n")
    elif level == 2:
        out.write("    <h2>" + abstract + "</h2>\n")

def list(out, item):
    out.write("          <li>" + item + "</li>\n")

def start_table(out, table, level):
    if level == 1:
        out.write("    <h1>" + table + "</h1>\n")
    elif level == 2:
        out.write("    <h2>" + table + "</h2>\n")
    out.write("      <table border='1'>\n");


def end_table(out, data):
    out.write("        <tr>\n")
    for d in data:
        out.write("          <th>" + d + "</th>\n")
    out.write("        </tr>\n")
    out.write("        <tr>\n")
    for d in data:
        out.write("          <th>&nbsp;</th>\n")
    out.write("        </tr>\n")

    out.write("      </table>\n")


def footer(out):
    out.write("  </body>\n")
    out.write("</html>\n")


def process(entrypoint, out_dn):

    relationships = tax.semantic.get_entrypoint_relationships(entrypoint)
    if relationships is None:
        print("Entry Point command line argument does not exist in Taxonomy.")
        sys.exit()

    with open(out_dn + "/" + entrypoint + ".html", "w") as out:
        header(out)

        first = True
        in_table = False
        level = 1
        data = []
        for r in relationships:
            f = r.from_.split(":")[1]
            t = r.to.split(":")[1]
            if first:
                abstract(out, f.replace("Axis", ""), level)
                first = False
                level += 1
                continue

            if in_table:
                if r.role.value == "hypercube-dimension":
                    data.append(t.replace("Axis", "") + " (PK)")
                elif r.role.value == "domain-member":
                    data.append(t)
                elif r.role.value == "all":
                    end_table(out, data)
                    data = []
            else:
                if r.role.value == "domain-member" and t.endswith("Abstract"):
                    abstract(out, t, level)
                elif r.role.value == "domain-member" and not t.endswith("Abstract"):
                    list(out, t)

            if t.endswith("Table"):
                start_table(out, t, level)
                in_table = True
                data = []

        if in_table:
            end_table(out, data)

        footer(out)


tax = taxonomy.Taxonomy()

if len(sys.argv) != 3:
    print("Incorrect number of arguments - 2 required")
    print("  Entrypoint")
    print("  Path to Output directory (example: ./somepath/outdir)")
    sys.exit(1)

entrypoint = sys.argv[1]
out_dn = sys.argv[2]

process(entrypoint, out_dn)
