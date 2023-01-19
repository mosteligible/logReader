docker-cleanup:
	docker rm $$(docker ps -aq)
	docker rmi -f $$(docker images --filter 'reference=logreader_*')

setup-db-image:
	echo "Environment variables CLIENT_DB_USERNAME \
CLIENT_DB_PASSWORD \
CLIENT_DB_TABLE_NAME \
CLIENT_ADD_TOKEN \
MYSQL_ROOT_PASSWORD \
must be set before running this target."
	bash ./MySQL_DB/setup_db.sh > ./MySQL_DB/db_setup.sql
	docker build -t mysql-db:1.0.0 -f ./MySQL_DB/Dockerfile.mysql ./MySQL_DB/

compose-logreader: setup-db-image
	docker-compose up --build
