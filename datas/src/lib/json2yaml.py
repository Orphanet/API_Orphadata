from pathlib import Path
import json
import requests
from typing import Dict, List
import time

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent
SCHEMAS_PATH = BASE_PATH / "api" / "swagger" / "schemas"
API_ROOT = "http://localhost:5000" # 'http://api.orphadata.com'

REQ = [
    {
        "url": "/rd-cross-referencing",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_full.yaml"
    },
    {
        "url": "/rd-cross-referencing/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_orphacodes.yaml"
    },
    {
        "url": "/rd-cross-referencing/orphacodes/58",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_by_orphacode.yaml"
    },
    {
        "url": "/rd-cross-referencing/orphacodes/names/marfan%20syndrome",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_by_name.yaml"
    },
    {
        "url": "/rd-cross-referencing/omims",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_omims.yaml"
    },
    {
        "url": "/rd-cross-referencing/omims/203450",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_by_omim.yaml"
    },
    {
        "url": "/rd-cross-referencing/icd-10s",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_icd-10s.yaml"
    },
    {
        "url": "/rd-cross-referencing/icd-10s/e75.2",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_by_icd10.yaml"
    },
    {
        "url": "/rd-cross-referencing/icd-11s",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_icd-11s.yaml"
    },
    {
        "url": "/rd-cross-referencing/icd-11s/4A44.5",
        "yaml_outfile": SCHEMAS_PATH / "cross_referencing" / "_by_icd11.yaml"
    },
    {
        "url": "/rd-classification",
        "yaml_outfile": SCHEMAS_PATH / "classification" / "_full.yaml"
    },
    {
        "url": "/rd-classification/hchids",
        "yaml_outfile": SCHEMAS_PATH / "classification" / "_hchids.yaml"
    },
    {
        "url": "/rd-classification/hchids/156/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "classification" / "_orphacodes_by_hchid.yaml"
    },
    {
        "url": "/rd-classification/hchids/181",
        "yaml_outfile": SCHEMAS_PATH / "classification" / "_by_hchid.yaml"
    },
    {
        "url": "/rd-classification/orphacodes/58/hchids",
        "yaml_outfile": SCHEMAS_PATH / "classification" / "_hchids_by_orphacode.yaml"
    },
    {
        "url": "/rd-classification/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "classification" / "_orphacodes.yaml"
    },
    {
        "url": "/rd-classification/orphacodes/58/hchids/181",
        "yaml_outfile": SCHEMAS_PATH / "classification" / "_by_orphacode_and_hchid.yaml"
    },
    {
        "url": "/rd-phenotypes",
        "yaml_outfile": SCHEMAS_PATH / "phenotypes" / "_full.yaml"
    },
    {
        "url": "/rd-phenotypes/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "phenotypes" / "_orphacodes.yaml"
    },
    {
        "url": "/rd-phenotypes/orphacodes/58",
        "yaml_outfile": SCHEMAS_PATH / "phenotypes" / "_by_orphacodes.yaml"
    },
    {
        "url": "/rd-phenotypes/hpoids",
        "yaml_outfile": SCHEMAS_PATH / "phenotypes" / "_hpoids.yaml"
    },
    {
        "url": "/rd-phenotypes/hpoids/HP:0000256,HP:0001249,HP:0001250,HP:0001257,HP:0002650,HP:0100729",
        "yaml_outfile": SCHEMAS_PATH / "phenotypes" / "_by_hpoid.yaml"
    },
    {
        "url": "/rd-associated-genes",
        "yaml_outfile": SCHEMAS_PATH / "genes" / "_full.yaml"
    },
    {
        "url": "/rd-associated-genes/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "genes" / "_orphacodes.yaml"
    },
    {
        "url": "/rd-associated-genes/orphacodes/166024",
        "yaml_outfile": SCHEMAS_PATH / "genes" / "_by_orphacode.yaml"
    },
    {
        "url": "/rd-associated-genes/genes",
        "yaml_outfile": SCHEMAS_PATH / "genes" / "_genes.yaml"
    },
    {
        "url": "/rd-associated-genes/genes/symbols/kif7",
        "yaml_outfile": SCHEMAS_PATH / "genes" / "_by_gene_symbol.yaml"
    },
    {
        "url": "/rd-associated-genes/genes/names/kinesin%20family",
        "yaml_outfile": SCHEMAS_PATH / "genes" / "_by_gene_name.yaml"
    },
    {
        "url": "/rd-medical-specialties",
        "yaml_outfile": SCHEMAS_PATH / "medical_specialties" / "_full.yaml"
    },
    {
        "url": "/rd-medical-specialties/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "medical_specialties" / "_orphacodes.yaml"
    },
    {
        "url": "/rd-medical-specialties/orphacodes/58",
        "yaml_outfile": SCHEMAS_PATH / "medical_specialties" / "_by_orphacode.yaml"
    },
    {
        "url": "/rd-medical-specialties/parents",
        "yaml_outfile": SCHEMAS_PATH / "medical_specialties" / "_parents.yaml"
    },
    {
        "url": "/rd-medical-specialties/parents/98006",
        "yaml_outfile": SCHEMAS_PATH / "medical_specialties" / "_by_parent.yaml"
    },
    {
        "url": "/rd-epidemiology",
        "yaml_outfile": SCHEMAS_PATH / "epidemiology" / "_full.yaml"
    },
    {
        "url": "/rd-epidemiology/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "epidemiology" / "_orphacodes.yaml"
    },
    {
        "url": "/rd-epidemiology/orphacodes/58",
        "yaml_outfile": SCHEMAS_PATH / "epidemiology" / "_by_orphacode.yaml"
    },
    {
        "url": "/rd-natural_history",
        "yaml_outfile": SCHEMAS_PATH / "natural_history" / "_full.yaml"
    },
    {
        "url": "/rd-natural_history/orphacodes",
        "yaml_outfile": SCHEMAS_PATH / "natural_history" / "_orphacodes.yaml"
    },
    {
        "url": "/rd-natural_history/orphacodes/58",
        "yaml_outfile": SCHEMAS_PATH / "natural_history" / "_by_orphacode.yaml"
    }
]


def json2yaml(obj):
    txt = []
    _map_type = {
        "int": "integer",
        "str": "string",
        "list": "array"
    }

    def _iterator(obj, indent=0):        
        if isinstance(obj, Dict):
            txt.append("{}type: object".format(' '*indent))
            if obj.keys():
                txt.append("{}properties:".format(' '*indent))
            for k, v in obj.items():
                txt.append("{}{}:".format(' '*(indent+2), k))
                _iterator(v, indent=indent+4)

        if isinstance(obj, List):
            txt.append("{}type: array".format(' '*indent))
            if not obj:
                txt.append("{}example: []".format(' '*indent))
            else:
                txt.append("{}items:".format(' '*indent))
                if [x for x in obj if isinstance(x, int) or isinstance(x, str)]:
                    txt.append("{}type: {}".format(' '*(indent+2), _map_type[type(obj[0]).__name__]))
                    txt.append("{}example: [{}]".format(' '*indent, ', '.join(map(str, obj[:3]))))
                else:
                    for item in obj[:1]:
                        _iterator(item, indent=indent+4)

        if isinstance(obj, str):
            txt.append("{}type: string".format(' '*indent))
            txt.append("{}example: \"{}\"".format(' '*indent, obj))


        if isinstance(obj, int):
            txt.append("{}type: integer".format(' '*indent))
            txt.append("{}example: {}".format(' '*indent, obj))

        if isinstance(obj, type(None)):
            txt.append("{}type: string".format(' '*indent))
            txt.append("{}example: null".format(' '*indent))

    _iterator(obj)

    return txt


for req in REQ[:]:
    url = API_ROOT + req.get("url")
    print("Requesting GET {} ...".format(url))
    response = requests.get(url=url)
    if not response.status_code == 200:
        print("Request did not succeed... Please check its URL or the server status.\n")
    else:
        response = response.json()

    print("Request succeeded.")
    print("Converting response to a yaml schema...")
    if response["data"]["__count"] > 3:
        response["data"]["results"] = response["data"]["results"][:3]

    try:
        yaml_schema = json2yaml(response)
    except:
        print("An error occured when converting json 2 yaml...".format())
        # exit()

    outfile = req.get("yaml_outfile")
    try: 
        outfile.parent.mkdir(parents=True, exist_ok=True)
    except:
        print("An error occured when creating {}".format(outfile.parent))
        break


    with open(outfile, "w") as _out:
        _out.write('\n'.join(yaml_schema))

    time.sleep(0.5)
