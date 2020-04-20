# API_Orphadata

# Technical documentation

## Software Version

The API description is written according to OpenAPI v3 standards.

The server stub has been auto-generated from the description
 with swagger-codegen version 3.0.19 in Python3-flask.

Developed with Elasticsearch 7.X.

Other modules requirement are referenced in 
python-flask-server-v3.requirements.txt:
    
    connexion == 2.6.0
    elasticsearch == 7.6
    python_dateutil == 2.6.0
    setuptools >= 21.0.0
    Flask-Testing >= 0.8.0

## Server setup

Create a server stub with the OpenAPI v3 description 
([swagger_v3_Orphadata](backup_manual_code/BU_swagger_v3_Orphadata.yaml))
with Python3-flask.

Two possibilities:
* Use the [online swagger-codegen](https://editor.swagger.io/)
(frequent new releases and features, potentially unstable)
* Use the [swagger-codegen-cli.jar](./tools/swagger-codegen-cli.jar)
from this distribution and follow the 
[swagger codegen instructions](./tools/swagger%20codegen%20instructions.txt)


/!\ Backup the manually created/edited files to 
[backup_manual_code](./backup_manual_code) /!\


Delete the [python-flask-server-generated](./python-flask-server-generated) folder and
replace it with the new version.

Check the content of the files from [backup_manual_code](./backup_manual_code)
(do not override because of the change made to the API contract, new modules or descriptions can be needed):
* "test" prefixed files must go to [python-flask-server-generated/swagger_server/test](./python-flask-server-generated/swagger_server/test)
* "_controller" suffixed files (except "test" prefixed files) 
must be compared to those in 
[python-flask-server-generated/swagger_server/controllers](./python-flask-server-generated/swagger_server/controllers)
* requirements.txt (do not override because new modules can be needed)
* config.py to [python-flask-server-generated-v3/swagger_server](./python-flask-server-generated/swagger_server)

The required packages can be installed by launching the following command
in the operating system's console (preferentially virtual environment console)
from the server's root [python-flask-server-generated-v3/swagger_server](./python-flask-server-generated/swagger_server)
    
    pip3 install -r requirements.txt
    pip3 install connexion[swagger-ui]

Note that 'test-requirements.txt' is auto generated and has not been used