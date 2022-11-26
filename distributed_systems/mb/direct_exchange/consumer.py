import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

queue = channel.queue_declare('direct_messages_queue')
queue_name = queue.method.queue

channel.queue_bind(exchange='postoffice_direct', queue=queue_name, routing_key='message_handlers')

def consume(ch, method, properties, body):
    print(f"\nReceived in Consumer: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=consume, queue=queue_name)

channel.start_consuming()
