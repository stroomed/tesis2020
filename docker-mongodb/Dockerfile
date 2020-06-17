FROM mongo:latest

RUN mkdir -p /data/info \
	&& echo "dbpath = /data/info" > /etc/mongodb.conf \
	&& chown -R mongodb:mongodb /data/info

COPY . /data/info

RUN mongod --fork --logpath /var/log/mongodb.log --dbpath /data/info --smallfiles \
	&& CREATE_FILES=/data/info/scripts/*-create.js \
	&& for f in $CREATE_FILES; do mongo 127.0.0.1:27017 $f; done \
	&& INSERT_FILES=/data/info/scripts/*insert.js \
	&& for f in $INSERT_FILES; do mongo 127.0.0.1:27017 $f; done \
	&& mongod --dbpath /data/info --shutdown \
	&& chown -R mongodb /data/info

VOLUME /data/info

CMD ["mongod", "--config", "/etc/mongodb.conf", "-smallfiles"]
