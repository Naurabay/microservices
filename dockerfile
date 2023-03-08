FROM python:3.10-slim-buster

COPY requirements.txt /

RUN pip install -r requirements.txt


RUN mkdir /app
WORKDIR /app

COPY service1.py /app
COPY sql_queries.py /app
COPY arrivals.py /app
COPY docker_test.py /app


CMD ["python", "/app/docker_test.py"]
