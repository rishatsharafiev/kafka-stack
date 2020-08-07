import random
import time

from confluent_kafka import Producer
from decouple import config


class SimpleProducer:
    kafka_conf = {
        'bootstrap.servers': config('KAFKA_BOOTSTRAP_SERVERS'),
    }
    kafka_producer = None

    def __init__(self) -> None:
        self.kafka_producer = Producer(self.kafka_conf)

    def run(self) -> None:
        counter = 1
        keys = [0, 1, 2]

        while True:
            key = str(random.choice(keys))
            message = f'value{counter}'
            self.kafka_producer.produce('simple_topic', message, key)
            counter += 1
            time.sleep(3)
            print(f'Sent message {key}:{message}')


def main():
    try:
        print('Start producer...')
        SimpleProducer().run()
    except KeyboardInterrupt:
        print('Stop producer...')


if __name__ == "__main__":
    main()
