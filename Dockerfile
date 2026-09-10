FROM python:3.14-alpine

COPY ./requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

COPY ./src /app

CMD python3 /app/app.py