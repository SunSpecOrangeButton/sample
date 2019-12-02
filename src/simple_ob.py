from oblib import taxonomy
from dataclasses import dataclass
from typing import List
import sys


@dataclass
class Child(object):
    pass


@dataclass
class Table(object):

    name: str
    pks: List[str]
    pk_values_enum: List[List[str]]
    members: List[str]
    children: List[Child]


@dataclass
class Abstract(Child):

    name: str
    members: List[str]
    tables: List[Table]
    children: List[Child]


@dataclass
class OB(object):

    abstracts: List[Abstract]
    tables: List[Table]


tax = taxonomy.Taxonomy()

def create_abstracts(entrypoint):

    relationships = tax.semantic.get_entrypoint_relationships(entrypoint)
    if relationships is None:
        print("Entry Point command line argument does not exist in Taxonomy.")
        return []

    abstracts = {}
    last_abstract = None
    last_table = None
    for r in relationships:
        f = r.from_.split(":")[1]
        t = r.to.split(":")[1]
        if r.role.value == "domain-member" and f.endswith("Abstract"):
            name = f.replace("Abstract", "")
            if name in abstracts:
                abstracts[name].members.append(t)
                last_abstract = abstracts[name]
            else:
                if t.endswith("LineItems"):
                    abstracts[name] = Abstract(name, [], None, None)
                else:
                    abstracts[name] = Abstract(name, [t], None, None)
                last_abstract = abstracts[name]
        elif r.role.value == "domain-member" and f.endswith("LineItems"):
            last_table.members.append(t)
        elif r.role.value == "domain-member" and f.endswith("Domain"):
            if last_table.pk_values_enum == None:
                last_table.pk_values_enum = [[]]
            last_table.pk_values_enum[0].append(t.replace("Member", ""))
        elif r.role.value == "all":
            if last_abstract.tables == None:
                last_abstract.tables = []
            last_table = Table(t, [], None, [], None)
            last_abstract.tables.append(last_table)
        elif r.role.value == "dimension-domain":
            pass
        elif r.role.value == "hypercube-dimension":
            last_table.pks.append(t.replace("Axis", ""))

    return abstracts

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Incorrect number of arguments - 2 required")
        print("  Entrypoint")
        sys.exit(1)

    entrypoint = sys.argv[1]
    abstracts = create_abstracts(entrypoint)
    for key in abstracts:
        print(abstracts[key])