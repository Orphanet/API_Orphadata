import json
from api import module_path

path2json = module_path / 'api' / 'swagger' / 'openapis'
with open(path2json / "openapi.json", "r") as _f:
    dic = json.load(_f)


dic["paths"] = {x:dic["paths"][x] for x in dic['paths'] if "rd-natural_history" in x }

tag_descr = "Natural history of rare diseases"
dic["tags"] = [x for x in dic["tags"] if tag_descr in x["name"]]


 

with open(path2json / "openapi_history.json", "w") as _f:
    _f.write(json.dumps(dic, indent=2))

