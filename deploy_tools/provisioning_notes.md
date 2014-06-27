Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com
* replace SERVER_USERNAME with the username/groupname for the sites
* replace PROJECT_NAME with the name of the django project

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/SERVER_USERNAME

/home/SERVER_USERNAME
|___ sites
    |___ SITENAME
         |--- database
         |--- source
         |--- static
         |___ virtualenv