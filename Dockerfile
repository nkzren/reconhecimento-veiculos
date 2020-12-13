FROM python:3.8-slim

RUN apt-get update && apt-get install -y \ 
    build-essential \
    cmake \
    gfortran \
    git \
    libatlas-base-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    libopencv-dev \
    libpng-dev \
    libtiff-dev \
    libvtk6-dev \
    pkg-config \
    python-dev \
    python-numpy \
    python-opencv \
    python-pycurl \
    qt5-default \
    unzip \
    webp \
    wget \
    zlib1g-dev \
    vim

WORKDIR /
COPY ./common ./common

WORKDIR /app

COPY ./app ./

RUN pip install -r ./requirements.txt

CMD [ "gunicorn", "-w 4", "-b", "0.0.0.0:8000", "main:app" ]

