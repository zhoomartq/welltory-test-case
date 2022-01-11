FROM python:3.8.10
ENV PYTHONUNBUFFERED 1

WORKDIR /welltr
RUN pip install --upgrade pip

COPY requirements.txt /welltr
RUN pip install -r /welltr/requirements.txt

ADD . /welltr/