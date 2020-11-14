FROM python:3.9.0-slim

ADD . /opt/person_server
WORKDIR /opt/person_server
ADD requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
