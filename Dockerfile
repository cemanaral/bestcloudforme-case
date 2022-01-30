# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

ENV FLASK_APP=main.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]