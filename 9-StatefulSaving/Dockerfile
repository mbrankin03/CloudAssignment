FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app
RUN pip3 install flask
RUN pip3 install tinydb
COPY ./src /app/
EXPOSE 5015
ENTRYPOINT ["python3"]
CMD ["app.py"]