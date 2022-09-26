import pika

import Config


class RabbitmqConfig:
    def __init__(self) -> None:
        self.host = Config.RABBITMQ_HOST
        self.port = Config.RABBITMQ_PORT
        self.vhost = Config.RABBITMQ_VHOST
        self.creds = pika.PlainCredentials(
            username=Config.RABBITMQ_USER, password=Config.RABBITMQ_PASSWORD
        )


class Sender:
    def __init__(self, config: RabbitmqConfig, clientId: str) -> None:
        self.config = config
        self.clientId = clientId
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.config.host,
                port=self.config.port,
                virtual_host=self.config.vhost,
                credentials=self.config.creds,
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=clientId)

    def send(self, message: str) -> None:
        self.channel.basic_publish(exchange="", routing_key=self.clientId, body=message)
