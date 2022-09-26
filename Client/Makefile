docker:
	docker build -t client-tracker:latest .
	docker run -d -p 80:80 --env-file client.env client-tracker:latest

local:
	uvicorn main:app

docker-stop:
	docker stop $$(docker ps -q --filter ancestor=client-tracker:latest)
	docker rm $$(docker ps -aq --filter ancestor=client-tracker:latest)
	docker rmi $$(docker images --filter "dangling=true")
