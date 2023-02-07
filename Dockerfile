FROM python:3.9.16-alpine3.16

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

EXPOSE 80

WORKDIR /app/appFlask/src

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
#ENTRYPOINT [ "python3", "/app/appFlask/src/app.py"]
CMD ["./entrypoint.sh"]
# cmd arrancar gunicorn
#CMD ["gunicorn"," --bind=0.0.0.0:80 app:app"]