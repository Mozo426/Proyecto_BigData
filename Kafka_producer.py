import time
import json
import random

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

while True:
    dato = dict(
        sensor_id=random.randint(1, 10),
        temperature=round(random.uniform(20, 30), 2),
        humidity=round(random.uniform(30, 70), 2),
        timestamp=int(time.time())
    )
    producer.send('sensor_data', value=dato)
    print("Enviado:", dato)
    time.sleep(1)
