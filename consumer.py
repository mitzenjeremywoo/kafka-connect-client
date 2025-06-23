import os
from kafka import KafkaConsumer

kafka_host = os.getenv('KAFKA_HOST')

# Connect to Kafka and subscribe to a topic
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=f'{kafka_host}:9092',
    auto_offset_reset='earliest',  # or 'latest'
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Listening for messages...")

for message in consumer:
    print(f"[{message.partition}] {message.offset} - {message.value}")
