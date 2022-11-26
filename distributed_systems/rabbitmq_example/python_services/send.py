import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='accounts', exchange_type='direct')

my_uuid = str(uuid.uuid4())

user = {
    'id': my_uuid,
    'user_email': f"{my_uuid[0:5]}@example.com"
}

channel.basic_publish(exchange='accounts', routing_key='user.welcome_email', body=json.dumps(user))
print('Asked WelcomeService to send welcome email')

channel.basic_publish(exchange='accounts', routing_key='user.profile_service', body=json.dumps(user))
print('Asked ProfileService to generate user profile')

connection.close()
