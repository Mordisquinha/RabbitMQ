import sys
import pika

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = "my_exchange"
        self.__routing_key = ""
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )
  
        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel

    
    def send_message(self, body:dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )


def get_input() -> str:
        if sys.argv[1]:
            input = sys.argv[1]
            cont = 2
            while True:
                try:
                    input += f" {sys.argv[cont]}"
                    cont += 1

                except:
                    break

        return input

body = get_input()
rabbitmq_consumer = RabbitmqPublisher()
rabbitmq_consumer.send_message(body)