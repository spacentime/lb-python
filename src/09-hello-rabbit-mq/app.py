import pika

eraGrouping = {
    'host' : 'xrpsldapprmq01a.unix.medcity.net',
    'username' : 'esscRmqDev',
    'password' : '69uFQFXqaO',
    'virtualhost' : 'essc',
    'queue' : 'eSSC.ERA.Queue',
    'exchange_event' : 'event',
    'exchange-retry': 'eSSC.ERA.Retry'
}

eDocPkg = {
    'host' : 'rabbitmq-bpaqa.svc.parallon.com',
    'username' : 'coresvc-med-rec',
    'password' : 'T27FvK<Om8mk',
    'virtualhost' : 'bpa',
    'queue' : 'eSSC.EDP.Queue.Local',
    'exchange_event' : 'eSSC.EDP',
    'exchange-retry': 'EDP.Local.Retry'
}  

eDocPkgParallon = {
    'host' : 'rabbitmq-bpaqa-amqp.svc.parallon.com',
    'username' : 'esscRmqQa',
    'password' : 'a8iThpDCWBbFwaZnjRUq',
    'virtualhost' : 'bpa',
    'queue' : 'para.fax',
    'exchange_event' : 'eSSC.EDP',
    'exchange-retry': 'EDP.Fax.Retry'
} 

# cfg = eraGrouping
cfg =  eDocPkg
# cfg = eDocPkgParallon

print(repr(cfg))

credentials = pika.PlainCredentials(cfg['username'], cfg['password'])
parameters = pika.ConnectionParameters(cfg['host'], virtual_host=cfg['virtualhost'], credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
queue = cfg['queue']
channel.queue_declare(queue=queue, durable=True, arguments={'x-dead-letter-exchange': cfg['exchange-retry']})

print(f'Publishing message to queue: {queue}')
channel.basic_publish(exchange=cfg['exchange_event'], routing_key=queue, body='Test Message')

print('Message sent successfully!')
connection.close()

