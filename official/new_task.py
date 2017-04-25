#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World!'
# msg_props = pika.BasicProperties()
# msg_props.content_type = "text/plain"
# channel.confirm_delivery()

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
    	delivery_mode=2
    ))

print(" [x] Sent %r" % message)
connection.close()
