FROM python:3.9-slim

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /app

#RUN python3 -m pip install psycopg2-binary
#RUN pip3 install setuptools && pip3 install -U setuptools
# pip installs
COPY ./app/requirements.txt requirements.txt

#RUN python3 -m pip install -U pip \
#  && python3 -m pip install -r /app/requirements.txt --no-cache-dir
#RUN apk add --no-cache postgresql-libs
RUN apt-get update \
 && apt-get install -y libpq-dev gcc
#RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN python3 -m pip install setuptools --upgrade \
 && pip install -r /app/requirements.txt --no-cache-dir

COPY . /app

#FastAPIの起動
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
