FROM python:3.10.0-alpine3.14
ENV PYTHONUNBUFFERED 1

# init alpine
RUN apk update && apk add --no-cache build-base \
                                     linux-headers \
                                     mariadb-connector-c-dev \
                                     bash \
                                     jq \
                                     jpeg-dev \
                                     curl && \
    pip install --upgrade pip

WORKDIR /var/www/html/seism-jp

# install modules
COPY requirements.txt .
RUN pip install -r requirements.txt
