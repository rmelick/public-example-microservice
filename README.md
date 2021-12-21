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
We use the postgres admin account for simplicity, so we do not need
to create users or give permissions (but that might look like the following)
from local dev postgres (docker exec)
```shell
createuser --pwprompt mydatabaseuser
createdb mydatabase -O mydatabaseuser

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
