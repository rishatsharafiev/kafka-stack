from confluent_kafka.admin import AdminClient, NewTopic
from decouple import config


admin_client = AdminClient({
    'bootstrap.servers': config('KAFKA_BOOTSTRAP_SERVERS')
})
new_topics = [
    NewTopic("simple_topic", num_partitions=3, replication_factor=3)
]
fs = admin_client.create_topics(new_topics)


for topic, f in fs.items():
    try:
        f.result()
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))
