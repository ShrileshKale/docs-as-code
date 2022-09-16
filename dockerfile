FROM python:3.8-slim-buster

LABEL maintainer="shrilesh.kale@betterask.erni"

WORKDIR /app

USER root

RUN pip install rstcloth 

RUN pip install -U sphinx


COPY . . 

CMD [ "python3" , "controller.py"]

