# Overview

This repository hosts all the code required to develop/maintain/update the [orphadata API](https://api.orphadata.com/).

The API
- gives a programmatic access to [Orphadata products](http://www.orphadata.org/cgi-bin/index.php). Data are monthly updated.

- is hosted on a [Gandi Simple Hosting](https://docs.gandi.net/fr/simple_hosting/connexion/git.html) instance.

- makes use of an **Elasticsearch server** instance to store and request data

- is served through the help of the python [Flask framework](https://flask.palletsprojects.com/en/2.0.x/). Flask is also used as a proxy to query the Elasticsearch server.

- documentation follows the [OpenAPI v3 specification](https://swagger.io/specification/) and has been generated with [Swagger](https://swagger.io/).


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

- `datas/`, a folder containing scripts and modules relative to the **processing of data** (download, conversion and elastic injection). This folder is used to get the orphadata and store them in an elasticsearh instance that is queried by the API. 

There is also:
- `static/`, a folder containing all static files used to serve the API. The only reason this folder is not in `api/` is related to the way the gandi server instance accesses static files.

- `requirements.txt`, a file used to install all required python libraries.

- `wsgi.py`, a python script used to run the application.


# Requirements

All this code has been developed and tested:

- on a UNIX OS system (but WSL(2) on Windows should be fine)
- with python >= 3.8

You will also need:
- a local elasticsearch instance (version 7.* - for development & test purposes)
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
| `FLASK_ENV` | `test`, `dev` or `production` | `production` | Used by the flask API application
| `DATA_ENV` |  `remote` or `local` | `remote` | Used for data processing (data injection into elasticsearch)


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

### Confidential environment variables

Access to the remote AWS elasticsearch instance (case where `FLASK_ENV=dev|production` and `DATA_ENV=remote`) requires its URL and associated login credentials.

To avoid writing sensitive informations on the source code, python-dotenv is used to access credentials from environment variables. Unlike the previous ones, environment variables relative to the remote elasticsearch access must be stored in a file arbitrarily called `.varenv`.


Create a file `.varenv` at the root of this repository and into it the following variables:
```bash
ELASTIC_URL=the_elastic_url_marc_gives_you
ELASTIC_USER=the_associated_elastic_user_id
ELASTIC_PASS=the_associated_elastic_passwword
```

Please note that **this file should never be shared/accessible so don't forget to add it to your `.gitignore`** if not already present. Morevoer, since **this file must be present on the gandi server instance**, you will have to [upload it](#sftp-varenv) to the remote server.


# Quickstart

## Run the application

From now on, considering your `.varenv` file is correctly set and `FLASK_ENV` is either not set or have the value `production` or `dev`, you can simply type `python wsgi.py` to run the application. 

It should now be accessible locally on your browser at the following URL:port address: http://127.0.0.1:5000.


## Deploy the application

### Add your gandi git remote repository to your git config
To deploy the application, if not already done, you'll first need to add the remote repository related to the Gandi host server to your git configurations:
```
git remote add gandi git+ssh://5815773.sd5.gpaas.net/default.git
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