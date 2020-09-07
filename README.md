# Pokemon Card Maker Back-end

As per conventions, commands to run in the terminal are prefixed with `$`. This symbol should not be typed.

## Setup

**This setup requires you to have a 64-bit python 3.7 and pip installed.**
A virtual environment will be used to install dependencies.

- Install pipenv with `$ pip install pipenv`
- Clone the project
- navigate to the project `$ cd pkm-card-maker-back`
- run `$ pipenv install --ignore-pipfile` this creates a new virtual environment and installs the dependencies as specified in the `pipenv.lock` file.
- Open the virtual environment with `$ pipenv shell`
- Create a database named `pkm`
- Copy the `.env.example` and rename it to `.env`
- Inside the `.env`, edit the incorrect variables to match yours
- Migrate the database
  - Run `$ python manage.py migrate`
- Run the server
  - Run `$ python manage.py runserver`
  
### Set up an OAuth2.0 Application
Go to Django admin and add a new Application with the following configuration:

- client_id and client_secret should be left unchanged
- user should be your superuser
- redirect_uris should be left blank
- client_type should be set to confidential
- authorization_grant_type should be set to 'Resource owner password-based'
- name can be set to whatever you'd like

### Troubleshooting

**If you get the error `ModuleNotFoundError: No module named 'MySQLClient'` while running the server, you need to install the mysqlclient.**

## Make sure you are running the 64 bit version of python  

If it does not work try to:
- Download the client for python version 'cp37' [here](https://pypi.org/project/mysqlclient/#files) (64bit) or [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) (32 and 64 bit)
- Install the client by running `pipenv install <path-to-file>`

### Pipenv

Pipenv is a tool to create and manage virtual environments and install dependencies and track their versions (including versions of sub-dependencies).
It is very similar to NPM in the way that it creates a Pipfile.lock and it allows install packages as dev dependencies.

To install a package use `$ pipenv install <package name>`. To install a dev dependency add the --dev flag.
[Find more info on Pipenv on the Pipenv project site](https://pipenv.pypa.io/en/latest/basics/). It is strongly recommended to read this documentation and familiarize yourself with how pipenv versioncontrol works.
