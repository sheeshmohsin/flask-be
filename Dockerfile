FROM python:3.8-alpine

WORKDIR /code

RUN apk update && \
    apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && apk add g++

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY src/ /code/

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000


CMD ["flask", "run"]
