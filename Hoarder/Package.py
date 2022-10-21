from threading import Lock
import pika

import Config
from Constants import SENDER_LOG_DIR
from Log import create_logger


class RabbitmqConfig:
    def __init__(self) -> None:
        self.host = Config.RABBITMQ_HOST
        self.port = Config.RABBITMQ_PORT
        self.vhost = Config.RABBITMQ_VHOST
        self.creds = pika.PlainCredentials(
            username=Config.RABBITMQ_USER, password=Config.RABBITMQ_PASSWORD
        )


class Sender:
    lock = Lock()

    def __init__(self, clientId: str) -> None:
        self.config = RabbitmqConfig()
        self.clientId = clientId
        self.logger = create_logger(
            log_location=SENDER_LOG_DIR, logger_name=clientId, file_name=f"{clientId}.log"
        )
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
        self.logger.info(f"{clientId} Sender initiated!!")

    def send(self, message: str) -> None:
        with self.lock:
            self.channel.basic_publish(exchange="", routing_key=self.clientId, body=message)
        self.logger.info(f"Sent message {message}")
