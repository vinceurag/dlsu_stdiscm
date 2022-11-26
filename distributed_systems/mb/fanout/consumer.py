import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

queue = channel.queue_declare('fanout_messages_queue')
queue_name = queue.method.queue

channel.queue_bind(exchange='postoffice_fanout', queue=queue_name)

def consume(ch, method, properties, body):
  print(f"\nReceived message: {body}")
  ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=consume, queue=queue_name)

channel.start_consuming()
