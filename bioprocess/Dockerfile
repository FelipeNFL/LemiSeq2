FROM python:latest

RUN ["apt-get", "update"]
RUN mkdir -p /src
WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src
RUN chmod +x tools/phd2fas
RUN chmod +x tools/phrap
RUN chmod +x tools/phred
EXPOSE 5001
