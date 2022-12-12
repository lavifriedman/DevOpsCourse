#!/bin/bash
list_of_containers=$(docker ps -a | awk '{print $1}')
for container in ${list_of_containers[@]}; do
	if [ $container != CONTAINER ]
	then
	docker stop $container
	docker rm  $container
	fi
done

