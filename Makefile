docker-cleanup:
	docker rm $$(docker ps -aq)
	docker rmi -f $$(docker images --filter 'reference=logreader_*')

setup-db-image:
	bash ./MySQL_DB/setup_db.sh || exit "$$?"

compose-logreader: setup-db-image
	docker-compose up --build
