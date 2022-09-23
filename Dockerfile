FROM python:3.10-alpine
WORKDIR /vacancy/
COPY requirements.txt /vacancy/
RUN pip install -r requirements.txt

COPY . /vacancy/

