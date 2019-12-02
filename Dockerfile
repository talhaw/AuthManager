FROM python:3.6

EXPOSE 5000

WORKDIR /AuthManager

COPY . /AuthManager
RUN pip install -r requirements.txt
