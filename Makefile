docker-cleanup:
	docker stop $$(docker ps -aq) && \
	docker rm $$(docker ps -aq) && \
	docker rmi -f $$(docker images --filter 'reference=logreader_*') && \
	docker system prune -f

setup-db-image:
	bash ./MySQL_DB/setup_db.sh || exit "$$?"

compose-logreader: setup-db-image
	docker compose up --build

tests:
	bash ./scripts/client_tests.sh
