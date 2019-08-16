FROM python:latest
WORKDIR /usr/src
ADD ./api /usr/src
RUN pip install -r requirements.txt
