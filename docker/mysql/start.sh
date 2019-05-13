#!/bin/bash
echo "create a mysql container.."
docker run -d --name mysql \
	   -v $(pwd)/conf.d:/etc/mysql/conf.d \
	   -v $(pwd)/data:/var/lib/mysql \
	   -e MYSQL_ROOT_PASSWORD="123456" \
	   -e MYSQL_DATABASE="muke" \
	   -p 3307:3306 \
	   mysql:5.7 \
	   --character-set-server=utf8 --collation-server=utf8_general_ci
