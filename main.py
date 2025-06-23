from kafka import KafkaProducer

def main():
    # Connect to Kafka broker
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    # Send a message to a topic
    producer.send('my-topic', b'Hello, Kafka!')

    # Optional: wait for all messages to be sent and close the producer
    producer.flush()
    producer.close()

if __name__ == "__main__":
    main()
