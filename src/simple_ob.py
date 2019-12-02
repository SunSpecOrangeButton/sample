from oblib import taxonomy
from dataclasses import dataclass
from typing import List
import sys

@dataclass
class Abstract:

    name: str
    members: List[str]
    is_table: bool
    pks: List[str]
    pk_legal_values: List[List[str]]

tax = taxonomy.Taxonomy()

def create_abstracts(entrypoint):

    relationships = tax.semantic.get_entrypoint_relationships(entrypoint)
    if relationships is None:
        print("Entry Point command line argument does not exist in Taxonomy.")
        return []

    abstracts = {}
    last_abstract = None
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
                    abstracts[name] = Abstract(name, [], False, None, None)
                else:
                    abstracts[name] = Abstract(name, [t], False, None, None)
                last_abstract = abstracts[name]
        elif r.role.value == "domain-member" and f.endswith("LineItems"):
            last_abstract.members.append(t)
        elif r.role.value == "domain-member" and f.endswith("Domain"):
            if last_abstract.pk_legal_values == None:
                last_abstract.pk_legal_values = [[]]
            last_abstract.pk_legal_values[0].append(t.replace("Member", ""))
        elif r.role.value == "all":
            last_abstract.is_table = True
        elif r.role.value == "dimension-domain":
            pass
        elif r.role.value == "hypercube-dimension":
            if last_abstract.pks == None:
                last_abstract.pks = []
            last_abstract.pks.append(t.replace("Axis", ""))

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