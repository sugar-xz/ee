FROM python:3.6

# env
ENV RUN_MODE=DEPLOY

RUN apt-get update
RUN apt-get install -y postgresql-client

ADD ./requirements.txt /tmp/
WORKDIR /tmp/
RUN pip install -r requirements.txt 

# add project to the image
ADD ./ /data/tavern/
WORKDIR /data/tavern/

# RUN server after docker is up
ADD ./start.sh /data/tavern/start.sh
RUN chmod 777 /data/tavern/start.sh
CMD ./start.sh
