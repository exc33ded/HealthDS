FROM python:3.8.10-alpine

WORKDIR /config/workspace/

ADD . /config/workspace/

RUN pip install -r requirements.txt

CMD ["python","app.py"]