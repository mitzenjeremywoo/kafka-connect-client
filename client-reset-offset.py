import os
from kafka import KafkaConsumer, TopicPartition

kafka_host = os.getenv('KAFKA_HOST')
bootstrap_servers = [f'{kafka_host}:9092']

topic = 'my-topic'
mygroup = 'my-group'
partition = 0
desired_offset = 1

# Create consumer without subscribing with enable auto commit false 
consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,   
                         group_id=mygroup)

# Assign specific partition
tp = TopicPartition(topic, partition)
consumer.assign([tp])

# Seek to desired offset
consumer.seek(tp, desired_offset)

# Start consuming from offset 1
for message in consumer:
    print(f"Offset: {message.offset}, Key: {message.key}, Value: {message.value}")
