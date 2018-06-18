FROM python:latest

RUN ["apt-get", "update"]
RUN mkdir -p /src
WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src
EXPOSE 5001
