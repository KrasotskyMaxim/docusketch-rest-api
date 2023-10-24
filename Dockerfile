FROM python:3.8
ADD . /docusketch-rest-api
WORKDIR /docusketch-rest-api
RUN pip install -r requirements.txt