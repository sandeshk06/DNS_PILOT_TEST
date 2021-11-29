FROM alpine:latest
LABEL maintainer="sandeshkulkarni1991@gmail.com"
RUN apk add --update python3 py3-pip
RUN pip3 install flask waitress ipaddress flask_wtf
COPY dns_validator.py   /usr/local/src/DNS_RESOLVER/
COPY dns_app.py   /usr/local/src/DNS_RESOLVER/
COPY templates   /usr/local/src/DNS_RESOLVER/templates/
COPY static   /usr/local/src/DNS_RESOLVER/static/
WORKDIR "/usr/local/src/DNS_RESOLVER/"
EXPOSE 5000
ENTRYPOINT python3 dns_app.py 
