import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='postoffice_topic', exchange_type='topic')

message = "A user has left: Vince"

channel.basic_publish(exchange='postoffice_topic', routing_key='user.left', body=message)
print('Published the message')

connection.close()
