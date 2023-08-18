FROM python:3.9

WORKDIR /zelus
COPY  . /zelus/
ENTRYPOINT ["python", "main.py"]