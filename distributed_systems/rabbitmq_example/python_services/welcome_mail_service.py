import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

queue = channel.queue_declare('welcome_email_queue')
queue_name = queue.method.queue

channel.queue_bind(exchange='accounts', queue=queue_name, routing_key='user.welcome_email')

def consume(ch, method, properties, body):
    payload = json.loads(body)
    print(f"\nWelcomeMailService successfully sent the welcome email to: {payload['user_email']}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=consume, queue=queue_name)

channel.start_consuming()
