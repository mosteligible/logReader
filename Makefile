docker-cleanup:
	docker rm $$(docker ps -aq)
	docker rmi -f $$(docker images -aq)
