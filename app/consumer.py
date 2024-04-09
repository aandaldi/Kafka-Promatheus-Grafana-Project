from kafka import KafkaConsumer
from json import loads
from time import sleep

consumer = KafkaConsumer(
    'first_topic',
    bootstrap_servers = ['localhost:9092'],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    group_id = 'my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
print("start")

for event in consumer:
    event_data = event.value
    print(event.key, " = ", event_data)
    sleep(3)