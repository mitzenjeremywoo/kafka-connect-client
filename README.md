
Creating the pod in kubernetes cluster

kubectl run python-pod --image=python:3.11-slim --restart=Never -it -- bash

To test interactively with a python container in kubernetes 

pip install kafka-python

Sample code

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='10.1.6.227 :9092')
producer.send('my-topic', b'Hello from Strimzi via port-forward!')
producer.flush()
producer.close()

