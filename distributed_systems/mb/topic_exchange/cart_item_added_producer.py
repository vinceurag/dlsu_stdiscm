import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange='postoffice_topic', exchange_type='topic')

message = "Item added"

channel.basic_publish(exchange='postoffice_topic', routing_key='cart.item_added', body=message)
print('Published the message')

connection.close()
