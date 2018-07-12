FROM node:8

RUN mkdir -p /front_end
WORKDIR /front_end

COPY package.json /front_end

RUN npm install

COPY . /front_end

EXPOSE 4200
