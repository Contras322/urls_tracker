FROM python:3.11.7-slim as app

ENV PYTHONUNBUFFERED 1

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip3 install --upgrade pip
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN pip install -r requirements.txt
COPY . /opt/app
