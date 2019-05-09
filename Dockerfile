FROM python:3.6.0

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
