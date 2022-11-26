import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='postoffice_direct', exchange_type='direct')

message = "Hello world!"

channel.basic_publish(exchange='postoffice_direct', routing_key='message_handlers', body=message)
print('Published the message')

connection.close()
