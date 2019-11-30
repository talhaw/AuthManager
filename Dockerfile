FROM python:3.6

EXPOSE 5000

WORKDIR /AuthManager

COPY . /AuthManager
RUN pip install -r requirements.txt


#COPY config.py /AuthManager
#COPY __init__.py /AuthManager
#COPY ./auth /app/AuthManager

CMD bash ./entrypoint/app.sh
