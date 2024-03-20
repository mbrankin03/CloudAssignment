FROM ruby:3.0.2-slim
COPY ./src /usr/src
WORKDIR /usr/src
RUN gem install webrick
EXPOSE 1234
ENTRYPOINT ["ruby"]
CMD ["app.rb"]