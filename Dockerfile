FROM python:3.6.6
WORKDIR /usr/src
ADD ./api /usr/src
#RUN apt-get update && apt-get install -y xmlsec1 libxmlsec1-dev pkg-config
RUN pip install -r requirements.txt
