# public-example-django
Simple django app for use in the docker-local-dev blog

#
```shell
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
from local dev postgres (docker exec)
```shell
createuser --pwprompt mydatabaseuser
createdb mydatabase -O mydatabaseuser

# enable the test user to create test databases
psql -c "alter user mydatabaseuser createdb" -d mydatabase

# migrate the database
./manage.py migrate
```

if you forgot to set the password of the database user
```shell
psql -c "ALTER ROLE super WITH PASSWORD 'mypassword'"
```
