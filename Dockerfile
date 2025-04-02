FROM python:3.9-alpine3.16

WORKDIR /app/

COPY requirements.txt app/

RUN pip install -r app/requirements.txt

COPY . app/

RUN apk add postgresql-client build-base postgresql-dev

EXPOSE 8000