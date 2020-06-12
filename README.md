# Reuirements

    1. Python - 3.6
    2. Node js - v12.18.0
    3. npm - 6.14.4
    4. Django - 2.2
    5. React js - 16.11.0
    6. MySQL - 5.7

# Instructions to setup Backend

    1. Create Python 3 virtual environment

        python3 -m venv /path/to/new/virtual/environment

    2. Activate virtual environment

        source /path/to/new/virtual/environment

    3. change directory to folder git_integration

    4. Install requirement.txt

        pip install -r requirement.txt

    5. create database

        create database DB_name;

    6. Change database settings in git_integration/settings.py


            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'DB_name',
                    'USER': 'username',
                    'PASSWORD': 'password',
                    'HOST': 'localhost',
                    'PORT': '3306',
                }
            }


    7. Run makemigrations and migrations command.


        python manage.py makemigrations
        python manage.py migrate

    8. Run following command to sync github issues to DB
            (You must be in git_integration folder)

        python manage.py sync_github_issues

    9. Run server

        python manage.py runserver

# Instructions to setup Frontend

    1. change directory to folder git_integration/frontend

        cd git_integration/frontend

    2. To install npm packages run:

        npm install

    3. To Bundle the React js modules using webpack run:

        ./node_modules/.bin/webpack --config webpack.config.js
