FROM php:7.2-apache
COPY . .
RUN ls
EXPOSE 2000
WORKDIR /var/www/html/src
CMD ["php", "-S", "0.0.0.0:2000"]
