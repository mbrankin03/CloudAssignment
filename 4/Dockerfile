FROM python:3.7

WORKDIR /app

COPY ./src /app/

RUN pip install flask
RUN pip install discord_webhook

EXPOSE 7007

ENTRYPOINT ["python3"]
CMD ["app.py"]
