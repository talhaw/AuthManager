FROM python:3.6

EXPOSE 5000

ADD . /AuthManager

COPY . /AuthManager

WORKDIR /AuthManager

RUN pip install -r requirements.txt
