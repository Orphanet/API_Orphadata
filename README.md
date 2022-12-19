# Overview

This repository hosts all the code required to develop/maintain/update the [orphadata API](https://api.orphadata.com/).

The API
- gives a programmatic access to [Orphadata products](http://www.orphadata.org/cgi-bin/index.php). Data are monthly updated.

- is hosted on a [Gandi Simple Hosting](https://docs.gandi.net/fr/simple_hosting/connexion/git.html) instance.

- makes use of an **Elasticsearch server** instance to store and request data

- is served through the help of the python [Flask framework](https://flask.palletsprojects.com/en/2.0.x/). Flask is also used as a proxy to query the Elasticsearch server.

- documentation follows the [OpenAPI v3 specification](https://swagger.io/specification/) and has been generated with [Swagger](https://swagger.io/).


## About orphadata

Only free orphadata are consumed through the API. Theses products are:

- `product1`: *Rare diseases and alignment with terminologies and databases*
- `product3`: *Clinical classifications of rare diseases*
- `product4`: *Phenotypes associated with rare diseases*
- `product6`: *Genes associated with rare diseases*
- `product7`: *Linearisation of rare diseases*
- `product9_prev`: *Epidemiology rare diseases*
- `product9_ages`: *Natural history rare diseases*


## Repository structure

Below is a global tree view of the repository.

<pre><font color="#3465A4"><b>.</b></font>
├── <font color="#3465A4"><b>api/</b></font>
├── <font color="#3465A4"><b>datas/</b></font>
├── README.md
├── requirements.txt
├── <font color="#3465A4"><b>static/</b></font>
└── wsgi.py
</pre>

The repository is made of two independent parts:
- `api/`, a folder containing all code relative to the **flask implementation of the API**.

- `datas/`, a folder containing scripts and modules relative to the **processing of data** (download, conversion and elastic injection). This folder is used to get the orphadata and store them in an elasticsearch instance that is queried by the API. 

There is also:
- `static/`, a folder containing all static files used to serve the API. The only reason this folder is not in `api/` is related to the way the gandi server instance accesses static files.

- `requirements.txt`, a file used to install all required python libraries.

- `wsgi.py`, a python script used to run the application.


# Requirements

All this code has been developed and tested:

- on a UNIX OS system (but WSL(2) on Windows should be fine)
- with python >= 3.8

You will also need:
- a local [elasticsearch instance](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) (version 7.* - for development & test purposes)
- an access to the AWS elasticsearch instance
- an access to the Gandi host server


# Installation

## 1 - Virtual environment setup

Although not strictly necessary, this step is highly recommended (it will allow you to work on different projects without having any conflict between different python package versions). 

First install virtualenv:
```bash
python3 -m pip install virtualenv
```

You can then generate a virtual environment as follows:
```bash
virtualenv -p python3 .env
```

This command will create a directory called `.env/` with the latest python3 version you have on your system. This directory has the following structure:
<pre><font color="#3465A4"><b>.env/</b></font>
├── <font color="#3465A4"><b>bin/</b></font>
└── <font color="#3465A4"><b>lib/python3.8/site-packages/</b></font>
</pre>

<a id="venv-activate"></a>
In order to make your virtual environment active, you have to type:
```bash
source .env/bin/activate
```

Once activated, your shell command line should be preceeded by the name of your environment in parenthesis.

From now on, every python package that will be installed with the `pip install` command will be stored in `.env/lib/python3.8/site-packages/`. If some binary scripts come with a given package, they will be stored in `.env/bin/`


If you want to get out of your virtual environment, simply type `deactivate`.


## 2 - Clone the repository

First clone the whole project:
```bash
git clone https://github.com/Orphanet/API_Orphadata.git
```

Once downloaded, make sure your virtual environment is [activated](#venv-activate) and type the following commands:
```bash
cd API_Orphadata
pip install -r requirements.txt
```


## 3 - Settings

### Public environment variables

Both the flask application and the data processing scripts make use of environment variables:

| Name | Accepted values | Default value | Role
|---|---|---|---|
| `FLASK_ENV` | `test`, `dev` or `production` | `production` | Only used by the flask API application
| `DATA_ENV` |  `remote` or `local` | `local` | Only used for the full data update process: `datas/src/orphadata_update.py`


The `FLASK_ENV` variable defines an object (see `api/config.py`) used to configure the flask instantiated application (through the parameter `config_name` of the factory function `create_app()` in `api/__init__.py`).
Basically, if:
- `FLASK_ENV=test`, the application will
    - have DEBUG and TESTING variables set at True
    - connect to a local elasticsearch instance (http://localhost:9200/) 
- `FLASK_ENV=dev`, the application will
    - have DEBUG variable set at True
    - connect to the remote AWS elasticsearch instance (see below) 
- `FLASK_ENV=production`, the application will
    - have DEBUG variable set at False
    - connect to the remote AWS elasticsearch instance (see below)


The `DATA_ENV` variable is used by `datas/src/orphadata_update.py` to define on which elasticsearch instance data will be
injected to. If:
- `DATA_ENV=remote`, data will be injected to the remote AWS elasticsearch instance
- `DATA_ENV=local`, data will be injected to the local elasticsearch instance (http://localhost:9200/)


Those two environment variables can be set in a UNIX-based system as follows:
```bash
export FLASK_ENV=dev
export DATA_ENV=local
```

In case the variables have not been set, the default value is used. 

<a id='env-variables'></a>

### Confidential environment variables

Access to the remote AWS elasticsearch instance (case where `FLASK_ENV=dev|production` and `DATA_ENV=remote`) requires its URL and associated login credentials.

To avoid writing sensitive informations on the source code, python-dotenv is used to access credentials from environment variables. Unlike the previous ones, environment variables relative to the remote elasticsearch access must be stored in a file arbitrarily called `.varenv`.


Create a file `.varenv` at the root of this repository and into it the following variables:
```bash
ELASTIC_URL=the_elastic_url_marc_gives_you
ELASTIC_USER=the_associated_elastic_user_id
ELASTIC_PASS=the_associated_elastic_passwword
```

Please note that **this file should never be shared/accessible so don't forget to add it to your `.gitignore`** if not already present. Moreover, since **this file must be present on the gandi server instance**, you will have to [upload it](#sftp-varenv) to the remote server.


# Quickstart

## Run the application

Let's consider at this stage you have not setup a local elasticsearch instance. The application will need to access the remote elasticsearch instance, so you'll need:
- `.varenv` file being correctly set up
- `FLASK_ENV` variable set to either `production` or `dev` or nothing (because default is `production`)

You can then simply type `python wsgi.py` to run the application. It should now be accessible locally on your browser at the following URL:port address: http://127.0.0.1:5000.


## Deploy the application

### Add your gandi git remote repository to your git config
To deploy the application, if not already done, you'll first need to add the remote repository related to the Gandi host server to your git configurations:
```
git remote add gandi git+ssh://5815773@git.sd5.gpaas.net/default.git
```

### Push your code on Gandi
Once added, you will be able to (after having commited your changes if there are) push your branch of interest as follows:
```bash
git push gandi your_branch_name
```
and then enter the password to access the Gandi server instance.


<a id="sftp-varenv"></a>

### Add the .varenv file to the Gandi server instance
Next, you'll need to add the `.varenv` file directly in the root directory of the repository in the Gandi server instance (`/lamp0/web/vhosts/default/`). Note that this file was not pushed with the source code from the preceding command `git push gandi your_branch_name` since the file must be in `.gitignore`. To add it the the Gandi server instance, you can use one of the [recommended sFTP client software](https://docs.gandi.net/en/simple_hosting/connection/sftp.html). 

 You can also connect to the instance with a command line. First make sure you are located where your `.varenv` file is on your local repository. Then type the following:

```bash
# connect to the gandi instance and go to /lamp0/web/vhosts/default/ (you'll have to enter your password)
sftp 5815773@sftp.sd5.gpaas.net:/lamp0/web/vhosts/default/
# you should see sftp>. Now you can place your local .varenv file to the remote instance you are connected to
put .varenv
# quit the instance
exit
```

### Deploy your code on Gandi
Now the Gandi remote repository can be deployed with the following command:
```bash
ssh 5815773@git.sd5.gpaas.net deploy default.git your_branch_name
```
and then enter the password to access the Gandi server instance.

## Update the remote git repository

After having done some change on a given branch, you can update the Marc's remote repository with the following:
```bash
git commit -am "Comment your changes"
git push origin your_branch_name
```

# Documentation

## Data

This section describes how to retrieve orphadata and inject them into an elasticsearch instance.

Source codes dedicated in processing data is located in the `datas/` folder:

<pre><font color="#3465A4"><b>API_Orphadata/datas/src/</b></font>
├── <font color="#3465A4"><b>lib</b></font>
├── orphadata_download.py
├── orphadata_generic.py
├── orphadata_injection.py
├── orphadata_update.py
└── orphadata_xml2json.py
</pre>


### Step 1: Download XML orphadata

Orphadata in XML format can simply be retrieved as follows:
```bash
python datas/src/orphadata_download.py
```

This command will write all XML retrieved files into `API_Orphadata/datas/xml_data/`.


**NOTE**

Each time orphadata are updated a JSON file is generated for each product. This JSON file contains detailed informations about its related product such as its size, its languages, or also the URL where it can be accessed. Thereby all orphadata products are retrieved in XML format from the URLs given in each of these product-related JSONs. 

JSONs URLs are stored in the `PATH_PRODUCTS_INFOS` variable found in `datas/src/lib/config.py`:

 - `product1`: http://www.orphadata.org/cgi-bin/free_product1_cross_xml.json
 - `product3`: http://www.orphadata.org/cgi-bin/free_product3_class.json
 - `product4`: http://www.orphadata.org/cgi-bin/free_product4_hpo.json
 - `product6`: http://www.orphadata.org/cgi-bin/free_product6_genes.json
 - `product7`: http://www.orphadata.org/cgi-bin/free_product7_linear.json
 - `product9_prev`: http://www.orphadata.org/cgi-bin/free_product9_prev.json
 - `product9_ages`: http://www.orphadata.org/cgi-bin/free_product9_ages.json


### Step 2: Convert XML orphadata to elastic-compatible JSON data

Before being injected into an elasticsearch instance, data must be parsed and written in an elasticsearch compatible JSON format. 

The conversion of XML orphadata into elasticsearch compatible JSON files is done with the following command:

```bash
python datas/src/orphadata_xml2json.py
```

This command will write all JSON files into `API_Orphadata/datas/json_data/`.


### Step 3: Inject JSON orphadata to elasticsearch

Now that we have JSON files, we can inject them into an elasticsearch instance.

If you are using your local elasticsearch instance make sure that it is running and accessible at `localhost:9200`:
```
nche@orphanet13:~$ curl localhost:9200
{
  "name" : "orphanet13",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "7ODmxFEVQh2-bQS3qWFHLg",
  "version" : {
    "number" : "7.17.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "bee86328705acaa9a6daede7140defd4d9ec56bd",
    "build_date" : "2022-01-28T08:36:04.875279988Z",
    "build_snapshot" : false,
    "lucene_version" : "8.11.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}

```

To inject your data, type the following command:
```bash
# for local elasticsearch instance (default ES url: http://127.0.0.1:9200)
python datas/src/orphadata_injection.py -url local

# for remote elasticsearch instance (reads .varenv to access ES url)
python datas/src/orphadata_injection.py -url remote
```


This will create an elastic index named according to each JSON file and prefixed with `orphadata_` (except for `orphadata_en_product3.json` which already contains the prefix). For instance, the elastic index for `en_product1.json` will be `orphadata_en_product1`.

You can check that those indices are now stored on your elasticsearch instance:
```bash
# for local elasticsearch instance
curl localhost:9200/_cat/indices

# for remote elasticsearch instance
curl --user $ELASTIC_USER:$ELASTIC_PASS $ELASTIC_URL:9243/_cat/indices
```

**NOTE**

The `orphadata_injection.py` can also be used with parameters:

```bash
(.env) nche@orphanet13:~/projects/API_Orphadata$ python datas/src/orphadata_injection.py -h
usage: orphadata_injection.py [-h] [-path [PATH]] [-match [MATCH]] [-index [INDEX]] [-url [{local,remote}]] [--print]

Bulk inject ORPHADATA products in ES

optional arguments:
  -h, --help            show this help message and exit
  -path [PATH]          Path or filename of JSON file(s)
  -match [MATCH]        String used to filter JSON filenames matching it (only if -path is a directory)
  -index [INDEX]        Name of the index to create
  -url [{local,remote}]
                        ES URL type: either 'local' or 'remote'
  --print               Print path of JSON files that will be processed
```

### Full update process

While running individual steps described above could be useful for development purpose, the whole process has been automatized for production purpose. First you have to set up the environment variable `DATA_ENV` to chose your elasticsearch instance:
- `export DATA_ENV=local` for your local elasticsearch instance
- `export DATA_ENV=remote` for the remote elasticsearch instance (requires [`.varenv`](#env-variables) to be set up too)
Note that instead of declaring the variable in a terminal, you can alternatively define it in the `.varenv` file.


The following command will execute sequentially steps 1, 2 and 3 in one shot:
```bash
python datas/src/orphadata_update.py
```

## Swagger definition

### Requirements
- [npm from node.js](https://nodejs.org/en/download/)
- [swagger-cli](https://www.npmjs.com/package/swagger-cli)


The API uses an interface based on [OpenAPI specification](https://swagger.io/specification/). For this, Flask reads through Connexion a `swagger.yaml` file containing all specifications of available requests:
```python
# API_Orphadata/api/__init__.py
def create_app(config_name):
    options = {'swagger_url': '/'}
    app = connexion.App(__name__, specification_dir='./swagger/', options=options)
    app.add_api('swagger.yaml', arguments={'title': 'API Orphadata'}, pythonic_params=True)
    ...
```

If you need to update the specifications (to update/remove/add an operation), it is recommended to do it through the following workflow:
1. go here `API_Orphadata/api/swagger/`
2. make your modifications in the template `_swagger_template.yaml`
3. update `swagger.yaml` from the template: `swagger-cli bundle _swagger_template.yaml -t yaml -o swagger.yaml`

Why ? Simply to avoid manually writing the schema response describing the response to each request.


### Add a new operation

In case you need to add a new operation, first follow the main workfow described above. When adding the specification of the new operation, **you don't need to specify the description schema of the response**.

After having updated the `swagger.yaml` from the template, you can automatically build the description of the schema response of this new operation from the response itself:
1. open `API_Orphadata/datas/src/lib/json2yaml.py`
2. add in the `REQ` list variable the following key-pair values with values related to the new operation:
```python
REQ = [
  {
          "url": "/rd-new-operation",  # relative path of your new operation (as specified in swagger.yaml). 
          "yaml_outfile": SCHEMAS_PATH / "tag-name-new-operation" / "_descr-name.yaml"  # absolute location of the output file that will contain the schema response
  },
  ...
]
```
3. save and close the file
4. make sure your flask server runs locally (-> http://localhost:5000) 
5. generate the schema response: `python API_Orphadata/datas/src/lib/json2yaml.py`
6. add in `_swagger_template.yaml` a pointer to the specification describing the schema response of the new operation:
```yaml
      responses:
        "200":
          description: Successful operation
          content:
            application/json:
              schema:
                $ref: './schemas/tag-name-new-operation/_descr-name.yaml'
```
7. update `swagger.yaml` from the template: `swagger-cli bundle _swagger_template.yaml -t yaml -o swagger.yaml`

### About `json2yaml.py`
```python
"""
Helper script used to build a swagger compatible schema description 
of responses from the defined requests. 

The script requires the API running on the local server (see API_ROOT variable)
to make the call to each requests defined in the 'REQ' variable.

The 'REQ' variable contains the list of all requests that will be called. 
For each request, the response in JSON format is converted in a 
swagger-compatible YAML format that will be used to describe/display 
the schema of the response. Please note that not all the content of 
the response is converted, only the minimim useful information (e.g. 
 only the 1st element of lists is converted).

"""
```