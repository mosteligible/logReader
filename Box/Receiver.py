from threading import Thread
import time
import pika

import Config
from Constants import RECEIVER_LOG_DIR
from Log import create_logger


class RabbitmqConfig:
    def __init__(self) -> None:
        self.host = Config.RABBITMQ_HOST
        self.port = Config.RABBITMQ_PORT
        self.vhost = Config.RABBITMQ_VHOST
        self.creds = pika.PlainCredentials(
            username=Config.RABBITMQ_USER, password=Config.RABBITMQ_PASSWORD
        )


class Receiver(Thread):
    def __init__(self, clientId: str) -> None:
        self.config = RabbitmqConfig()
        self.clientId = clientId
        self.logger = create_logger(
            log_location=RECEIVER_LOG_DIR,
            logger_name=clientId,
            file_name=f"{clientId}.log"
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
        self.channel.basic_consume(
            queue=self.clientId,
            on_message_callback=self.callback,
        )

    def run(self) -> str:
        self.channel.start_consuming()

    @staticmethod
    def callback(self, ch, method, properties, body: str):
        body = body.decode('utf8')
        print(f"{self.clientId}: {body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        time.sleep(0.15)
