# public-example-django
A variation on the django app, for use in the docker-local-dev blog.

1. Uses mysql instead of postgres
2. Makes a call to the main webapp to simulate being a microservice

Related repositories:
* [public-docker-local-dev](https://github.com/vidahealth/public-docker-local-dev) is the main repository for the local dev environment
* https://github.com/vidahealth/public-example-django is the example main backend webserver service
* [public-example-microservice](https://github.com/vidahealth/public-example-microservice) (this respository) is an example of a "microservice" that makes calls back to the main backend web service

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
```


```shell
# migrate the database
./manage.py migrate
```

```shell
./manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: password
```
