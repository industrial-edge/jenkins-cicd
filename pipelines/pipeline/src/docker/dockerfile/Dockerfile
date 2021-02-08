FROM ubuntu:20.04
	
RUN apt-get update
	
COPY ie-app-publisher-linux /usr/bin

RUN apt-get install -y curl gnupg2 pass
RUN curl -sSL https://get.docker.com/ | sh
RUN apt-get install -y docker-compose

RUN mkdir -p /app/src/workspace
WORKDIR /app/src/workspace
RUN ie-app-publisher-linux ws init



