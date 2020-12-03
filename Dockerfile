FROM python:3.8-alpine

COPY ./main.py ./
COPY ./requirements.txt ./

RUN pip3 install -r ./requirements.txt

CMD [ "gunicorn", "-w 4", "-b", "0.0.0.0:8000", "main:app" ]

