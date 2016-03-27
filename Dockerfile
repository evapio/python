FROM iron/python:2-dev

MAINTAINER "Evap Engineering" info@evap.io

WORKDIR /code
RUN pip install tornado pymongo
EXPOSE 9090

CMD python -m tornado.autoreload /code/server.py