FROM python:3.8-alpine

# RUN mkdir app
WORKDIR /app

COPY ./main.py ./
COPY ./requirements.txt ./

RUN apk add --update make cmake gcc g++ gfortran libc-dev
RUN pip3 install opencv-python
RUN pip3 install -r ./requirements.txt

CMD [ "gunicorn", "-w 4", "-b", "0.0.0.0:8000", "main:app" ]

