FROM python:3

MAINTAINER tanvir002700@gmail.com

RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
     build-essential \
     python3-dev \
     libevent-dev \
    && rm -rf /var/lib/apt/lists

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD python api/manage.py runserver 0.0.0.0:8000
