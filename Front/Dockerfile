FROM php:7.2-apache
COPY src/ /var/www/html/
EXPOSE 80

# Set the ServerName to suppress the Apache warning
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
