from confluent_kafka import Consumer
from decouple import config


class SimpleConsumer:
    kafka_conf = {
        'bootstrap.servers': config('KAFKA_BOOTSTRAP_SERVERS'),
        'group.id': 'simple_group',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': 'false',
        'auto.offset.reset': 'earliest',
    }
    kafka_consumer = None

    def __init__(self) -> None:
        self.kafka_consumer = Consumer(self.kafka_conf)

    def proccess_messages(self, messages):
        for message in messages:
            if message is None:
                continue

            message_error = message.error()
            if message_error:
                print('consumer_message_warning', message_error)
                continue

            yield message

    def consume(self, kafka_consumer, num_messages=1000, timeout=1.0):
        try:
            while True:
                messages = kafka_consumer.consume(
                    num_messages=num_messages, timeout=timeout
                )
                for message in self.proccess_messages(messages):
                    yield message
        finally:
            kafka_consumer.close()

    def run(self) -> None:
        kafka_consumer = self.kafka_consumer
        kafka_consumer.subscribe(['simple_topic'])

        for message in self.consume(kafka_consumer):
            message_value = message.value().decode('utf-8')
            print(f'Message: {message_value}')
            kafka_consumer.commit(message=message, asynchronous=False)


def main():
    try:
        print('Start consumer...')
        SimpleConsumer().run()
    except KeyboardInterrupt:
        print('Stop consumer...')


if __name__ == "__main__":
    main()
