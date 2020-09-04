# API_Orphadata

Ver: august 2020

Author: Cyril Bigot

# Technical documentation

## Software Version

The API description is written according to OpenAPI v3 standards.

The server stub has been auto-generated from the description
 with swagger-codegen version 3.0.21 in Python3-flask.
 More information about swagger-codegen is available in the README.md shipped with the server stub.

Developed with Elasticsearch 7.X.

Other modules requirement are referenced in [requirements.txt](requirements.txt)

## Server setup

Create a server stub with the OpenAPI v3 description 
([swagger API orphadata](backup_manual_code/swagger API orphadata.yaml))
with Python3-flask.

Two possibilities:
* Use the [online swagger-codegen](https://editor.swagger.io/)
(frequent new releases and features, potentially unstable)
* Use the [swagger-codegen-cli.jar](./tools/generator 3.0.16/swagger-codegen-cli.jar)
from this distribution with the following command


    java -jar ./swagger-codegen-cli.jar generate -i ./my_API.yaml -l python-flask -o ./python_server

Backup [swagger_server](./swagger_server).

One convenient way to deploy a new stub is to create a new branch to do 
a MANUAL merge with pycharm "VCS/Git/compare with branch"

The required packages can be installed by launching the following command
in the operating system's console (preferentially virtual environment console)
from the server's root [swagger_server](swagger_server)
    
    pip3 install -r requirements.txt

Note that 'test-requirements.txt' is auto generated and has not been used

## Authorization by APIkey:
Mandatory in request header:

* any string for user level

        curl -X GET "http://api.orphacode.org/.../..."
             -H  "accept: application/json"
             -H  "apiKey: anything"
## Authorization by APIkey:
Mandatory in request header:
* "admin" for admin level
    
        curl -X GET "http://localhost:8080/orphaclassif/list_hchid"
             -H  "accept: application/json"
             -H  "ADMIN-API-KEY: admin"

* "test" for user level

        curl -X GET "http://localhost:8080/orphaclassif/list_hchid"
             -H  "accept: application/json"
             -H  "SIMPLE-API-KEY: test"

## Usage
Online, the server will call [wsgi.py](wsgi.py) as an entry point, it only
 reference the main application.

[swagger_server/API_main.py](swagger_server/API_main.py) is the Connexion/Flask object, 
you can pass additional options (see Flask documentation).

Then the application loads the API contract processed by the swagger-codegen.
[swagger_server/swagger/swagger.yaml](swagger_server/swagger/swagger.yaml)

The User Interface (UI) is generated from [swagger_server/template/index.j2](swagger_server/template/index.j2)
with jinja2 template generator.
The UI will loads the necessary javascript and CSS property from the
 swagger-ui python module.
The images are served from a folder at the root of the online server,
 meaning at the same directory level than swagger_server,
in a folder named [media](media). It is not possible to change the authorizations path
 for gandihost server so this folder has to be separated from the flask server.
The media files path must be referenced by "./media/". Thus it will not work directly in 
development, you can use the special media route for this, comment for production server.

#### API operation controllers
The API operations are located in the [swagger_server/controllers](swagger_server/controllers)
directory.

Their name are generated from the swagger-codegen from the operations
tags defined in the yaml file. They can contain symbols that are poorly
converted to the pythonic name convention and can be invalid.
Theses files need to be manually renamed and the 
[swagger_server/swagger/swagger.yaml](swagger_server/swagger/swagger.yaml)
need to be renamed accordingly.

* authorization_controller.py

    Will handle the apiKey check.
* query_controller

    Collection of functions needed to perform the query with elasticsearch.
    Because of the way elasticsearch return result, you need to slightly adjust
    the treatment of data.
    Depending of the amount of data you expect to return,
    you can choose to use:
    * single_res for a single result
    * multiple_res for a reasonable number of results (N << 10000)
    * uncapped_res for an higher number
       
      This method will use the "scroll" function of elastic search and will
      cost more resources.
      
    Also contains a function to convert the API response to YAML.
    
* other controllers
    
    Fulfills the corresponding operation.
    Don't forget to test for an error if you need to process the
    result of query controller.