FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt -y install iputils-ping wget ca-certificates mosquitto-clients

COPY CA/wisca.crt /usr/local/share/ca-certificates
RUN update-ca-certificates
