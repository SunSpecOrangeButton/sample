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
import simple_ob

import sys


def header(out):
    out.write("<html>\n")
    out.write("""
    <header>
        <style>
              .outer {
                  margin: 0 auto;
                }
                
                .inner {
                  margin-left: 50px;
                }
            </style>
        </header>
    """);
    out.write("  <body>\n")


def abstract(out, abstract, level):
    if level == 1:
        out.write("    <h1>" + abstract + " (A)</h1>\n")
    elif level == 2:
        out.write("    <h2>" + abstract + " (A)</h2>\n")

def start_list(out):
    out.write("          <ul>\n")

def list(out, item):
    out.write("          <li>" + item + "</li>\n")

def end_list(out):
    out.write("          </ul>\n")

def start_table(out, table, level):
    # if level == 1:
    #     out.write("    <h1>" + table + " (T)</h1>\n")
    # elif level == 2:
    out.write("    <h2>" + table + " (T)</h2>\n")
    out.write("      <table border='1'>\n");


def end_table(out, data, legal_values):
    out.write("        <tr>\n")
    for d in data:
        out.write("          <th>" + d + "</th>\n")
    out.write("        </tr>\n")
    if legal_values == None:
        out.write("        <tr>\n")
        for d in data:
            out.write("          <td>&nbsp;</td>\n")
        out.write("        <tr>\n")
    else:
        max_count = 0
        for lv in legal_values:
            if len(lv) > max_count:
                max_count = len(lv)

        for i in range(0, max_count):
            out.write("        <tr>\n")
            for lv in legal_values:
                if len(lv) > i:
                    out.write("          <td>" + lv[i] + "</td>\n")
                else:
                    out.write("          <td>&nbsp;</td>\n")
            for ii in range(len(legal_values), len(data)):
                out.write("          <td>&nbsp;</td>\n")
            out.write("        <tr>\n")
    out.write("      </table>\n")


def footer(out):
    out.write("  </body>\n")
    out.write("</html>\n")


def process(entrypoint, out_dn):

    abstracts = simple_ob.create_abstracts(entrypoint)

    level = 1
    with open(out_dn + "/" + entrypoint + ".html", "w") as out:
        header(out)
        for key in abstracts:
            abstract(out, key, level)
            a = abstracts[key]
            start_list(out)
            for member in a.members:
                list(out, member)
            end_list(out)

            if a.tables:
                for t in a.tables:
                    start_table(out, t.name, level)
                    data = []
                    for pk in t.pks:
                        data.append(pk + " (PK)")
                    for member in t.members:
                        data.append(member)
                    end_table(out, data, t.pk_values_enum)
            if level == 1:
                level = 2

        footer(out)


tax = taxonomy.Taxonomy()

if len(sys.argv) != 3:
    print("Incorrect number of arguments - 2 required")
    print("  Entrypoint (ALL creates all entrypoints")
    print("  Path to Output directory (example: ./somepath/outdir)")
    sys.exit(1)

entrypoint = sys.argv[1]
out_dn = sys.argv[2]

if entrypoint.lower() == "all":
    for entrypoint in tax.semantic.get_all_entrypoints():
        if entrypoint.lower() != "all":
            print("Creating", entrypoint)
            process(entrypoint, out_dn)
else:
    process(entrypoint, out_dn)
