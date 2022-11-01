FROM python:3.8-slim-buster

LABEL maintainer="shrilesh.kale@betterask.erni"

WORKDIR /app

USER root

RUN pip install rstcloth 

RUN pip install -U sphinx==3.3.1

RUN pip install pandas

RUN pip install python-docx

RUN pip install simplify-docx

RUN pip install pdf2docx

COPY . . 

CMD [ "python3" , "controller.py"]

