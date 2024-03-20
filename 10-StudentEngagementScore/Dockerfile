FROM golang:1.14
WORKDIR /go/src/app
COPY . .
RUN cd src && go build -o main .
EXPOSE 2023
ENTRYPOINT ["./src/main"]