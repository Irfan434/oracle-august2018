
# Irfan Ahmad's solution for Oracle Technical Interview

I implemented the REST service using the python Django framework.

It can be downloaded as follows:
* visit https://github.com/Irfan434/oracle-august2018
* OR run: `docker pull irfan434/oracle-august2018`

Upon starting docker, you may get a message like:
```
docker is configured to use the default machine with IP 192.168.99.100
```
Take note of this IP address.

Then run:
```
docker-compose up.
```
Ignore any messages about unapplied migrations, since this service does not use a database.

Then, head to your web browser and enter the URL http://192.168.99.100:8000/stringService/stringClean/abbbcdd, which should return *abcd*.

The REST endpoints are:
* http://[YOUR IP HERE]/stringService/stringClean/[INPUT STRING]
* http://[YOUR IP HERE]/stringService/maxBlock/[INPUT STRING]
* http://[YOUR IP HERE]/stringService/reorderBlock/[INPUT STRING]

## Contact
Email: irfana572 AT gmail DOT com

## References
* Django Tutorial
  * https://docs.djangoproject.com/en/2.0/intro/tutorial01/
* Using Docker with Django
  * https://docs.docker.com/compose/django/
* Case-insensitive sorting in python
  * https://stackoverflow.com/questions/10269701/case-insensitive-list-sorting-without-lowercasing-the-result