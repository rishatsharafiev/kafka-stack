# kafka-stack

Запуск кластера
```
cd kafka
docker-compose -f full-stack.yml -p kafka-stack-full-stack up
```

Открыть kafka-topics
```
browse http://localhost:8000
```

```
# продьюсер с ключом
./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic --property "parse.key=true" --property "key.separator=:"

# продьюсер без ключа
./bin/kafka-console-producer.sh --broker-list localhost:9092,localhost:9093,localhost:9094 --topic my-topic

# создать топик
./bin/kafka-topics.sh --create --topic my-topic --replication-factor 3 --partitions 3 --zookeeper localhost:2181

# показать свойства топика
./bin/kafka-topics.sh --zookeeper localhost:2181 -- topic my-topic --describe
```