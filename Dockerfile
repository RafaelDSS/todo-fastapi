FROM python:3.8.3-slim-buster

WORKDIR /wiretrack/ 

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip &&  pip install -r requirements.txt

COPY . .
