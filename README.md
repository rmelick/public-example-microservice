# public-example-django
A variation on the django app
1. Uses mysql instead of postgres
2. Makes a call to the main webapp to simulate being a microservice

#
```shell
pyenv virtualenv 3.9.7 example-microservice
pip install -r requirements.txt

django-admin startproject tutorial
cd tutorial
./manage.py startapp quickstart

```
Followed DRF quickstart
https://www.django-rest-framework.org/tutorial/quickstart/

# testing
when deployed with PyCharm
```shell
curl localhost:8000/status
```

# setting up database
We use the postgres admin account for simplicity, so we do not need
to create users or give permissions (but that might look like the following)
from local dev mysql (docker exec)
```shell
mysql -p
CREATE DATABASE microservicedb;

# enable the test user to create test databases
psql -c "alter user mydatabaseuser createdb" -d mydatabase
```

if you forgot to set the password of the database user
```shell
psql -c "ALTER ROLE mydatabaseuser WITH PASSWORD 'mypassword'"
```

```shell
# migrate the database
./manage.py migrate
```

```shell
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: password
```
