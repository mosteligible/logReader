FROM alpine:3.14

WORKDIR /app

COPY . /app

RUN apk add --update --no-cache python3 && \
    ln -sf python3 /usr/bin/python && \
    apk add curl
RUN python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip install --upgrade pip &&\
    pip install -r requirements.txt --no-cache-dir

CMD python main.py
