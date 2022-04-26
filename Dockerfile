FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . /opt/graphene_timescale/
WORKDIR /opt/graphene_timescale/src

EXPOSE 8000

CMD ./manage.py migrate && ./manage.py runserver 0.0.0.0:8000
