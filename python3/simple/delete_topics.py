from confluent_kafka.admin import AdminClient
from decouple import config


admin_client = AdminClient({
    'bootstrap.servers': config('KAFKA_BOOTSTRAP_SERVERS')
})
delete_topics = ["simple_topic"]
fs = admin_client.delete_topics(delete_topics)


for topic, f in fs.items():
    try:
        f.result()
        print("Topic {} deleted".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))
