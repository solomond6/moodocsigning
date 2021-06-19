FROM python:3.7.7-buster

RUN wget -O - http://nginx.org/keys/nginx_signing.key | apt-key add - && \
echo "deb http://nginx.org/packages/debian/ buster nginx" | tee -a /etc/apt/sources.list && \
echo "deb-src http://nginx.org/packages/debian/ buster nginx" | tee -a /etc/apt/sources.list
RUN apt-get update -o Acquire::CompressionTypes::Order::=gz && apt-get install -y  nginx supervisor pdftk && \
echo "daemon off;" >> /etc/nginx/nginx.conf && mkdir /var/log/favorite_things/
RUN apt-get install curl && curl -sL https://deb.nodesource.com/setup_12.x | bash - && apt-get -y install nodejs
WORKDIR /usr/src/app/
COPY requirements.txt /usr/src/app/requirements.txt
ARG ENV

RUN pip install --upgrade pip && pip install gunicorn && pip install -r requirements.txt
COPY . /usr/src/app/

RUN bash -c "chmod +x ./docker/run.sh"

EXPOSE 8000 90 80

CMD ["./docker/run.sh"]