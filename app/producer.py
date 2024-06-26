
import random 
import string
import time 
import json 
import random 
from datetime import datetime
from kafka import KafkaProducer


user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()
    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)
    # Generate a random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))
    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message
    }


# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9093'],
    key_serializer=serializer,
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        key = f'{datetime.now()}'.replace(':','').replace('-','').replace('.','').replace(' ','')[0:14]
        # Generate a message
        dummy_message = generate_message()

        topic_name = "first_topic"
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Key = {key} | Message = {str(dummy_message)}')
        producer.send(topic_name, key=int(key), value=dummy_message)
        producer.flush()
        
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(15, 30)
        time.sleep(time_to_sleep)

