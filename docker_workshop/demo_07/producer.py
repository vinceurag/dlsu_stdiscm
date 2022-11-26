import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='postoffice_fanout', exchange_type='fanout')

message = "Hello world!"

channel.basic_publish(exchange='postoffice_fanout', routing_key='', body=message)
print('Published the message')

connection.close()
