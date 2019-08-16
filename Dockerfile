FROM python:3.6.6
WORKDIR /usr/src
ADD ./api /usr/src
RUN pip install -r requirements.txt
