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


class Base():

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

    def footer(out):
        out.write("  </body>\n")
        out.write("</html>\n")

    def abstract(out, abstract, level):
        out.write("    <h" + str(level) + ">" + abstract + " (Abstract)</h" + str(level) + ">\n")

    def start_list(out):
        out.write("          <ul>\n")

    def list(out, item):
        out.write("          <li>" + item + "</li>\n")

    def end_list(out):
        out.write("          </ul>\n")


class TableHRepresentation(Base):

    def start_table(out, table, level):
        # if level == 1:
        #     out.write("    <h1>" + table + " (T)</h1>\n")
        # elif level == 2:
        out.write("    <h2>" + table + " (T)</h2>\n")
        out.write("      <table border='1'>\n")

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


    def process(entrypoint, out_dn):

        abstracts = simple_ob.create_abstracts(entrypoint)

        with open(out_dn + "/" + entrypoint + "-h.html", "w") as out:
            TableHRepresentation.header(out)
            for key in abstracts:
                TableHRepresentation.subprocess(abstracts[key], 1, out)
                break
            TableHRepresentation.footer(out)

    def subprocess(a, level, out):
        TableHRepresentation.abstract(out, a.name, level)
        TableHRepresentation.start_list(out)
        for member in a.members:
            TableHRepresentation.list(out, member)
        if a.tables:
            for t in a.tables:
                TableHRepresentation.start_table(out, t.name, level)
                data = []
                for pk in t.pks:
                    data.append(pk + " (PK)")
                for member in t.members:
                    data.append(member)
                TableHRepresentation.end_table(out, data, t.pk_values_enum)
                if t.children:
                    for c in t.children:
                        TableHRepresentation.subprocess(c, level+1, out)
        if a.children:
            for c in a.children:
                if c is not None:
                    TableHRepresentation.subprocess(c, level+1, out)
        TableHRepresentation.end_list(out)


class TreeVRepresentation(Base):

    def start_table(out, table, level):
        out.write("    <h2>" + table + " (Table)</h2>\n")
        out.write("      <table border='1'>\n")

    def end_table(out, data, legal_values):
        out.write("        <tr>\n")
        out.write("          <th>Concept</th><th>Purpose</th>\n")
        out.write("        <tr>\n")

        col = 0
        for d in data:
            c = d
            p = "Data Element"
            if d.find("(PK)") != -1:
                c = d.replace("(PK)", "")
                p = "PK"
                if legal_values != None and len(legal_values[col]) > 0:
                    p = "PK - Set to one of:<br/>"
                    for l in legal_values[col]:
                        p += "&nbsp;&nbsp;" + l + "<br/>"
            elif d.find("(A)") != -1:
                c = d.replace("(A)", "")
                p = "Abstract"

            out.write("        <tr>\n")
            out.write("          <td>" + c + "</td><td>" + p + "</td>\n")
            out.write("        <tr>\n")
            col += 1

        out.write("      </table>\n")


    def process(entrypoint, out_dn):

        abstracts = simple_ob.create_abstracts(entrypoint)

        with open(out_dn + "/" + entrypoint + "-v.html", "w") as out:
            TreeVRepresentation.header(out)
            for key in abstracts:
                TreeVRepresentation.subprocess(abstracts[key], 1, out)
                break
            TreeVRepresentation.footer(out)

    def subprocess(a, level, out):
        TreeVRepresentation.abstract(out, a.name, level)
        TreeVRepresentation.start_list(out)
        for member in a.members:
            TreeVRepresentation.list(out, member)
        if a.tables:
            for t in a.tables:
                TreeVRepresentation.start_table(out, t.name, level)
                data = []
                for pk in t.pks:
                    data.append(pk + " (PK)")
                for member in t.members:
                    data.append(member)
                TreeVRepresentation.end_table(out, data, t.pk_values_enum)
                if t.children:
                    for c in t.children:
                        TreeVRepresentation.subprocess(c, level+1, out)
        if a.children:
            for c in a.children:
                if c is not None:
                    TreeVRepresentation.subprocess(c, level+1, out)
        TreeVRepresentation.end_list(out)


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
            TableHRepresentation.process(entrypoint, out_dn)
            TreeVRepresentation.process(entrypoint, out_dn)
else:
    TableHRepresentation.process(entrypoint, out_dn)
    TreeVRepresentation.process(entrypoint, out_dn)
