import nsq
import tornado.ioloop
import threading
import queue

queue = queue.Queue()


def process_message(message):
    message.enable_async()
    # cache the message for later processing
    queue.put(message)
    tornado.ioloop.IOLoop.current().call_later(0.1, pub_message)


def pub_message():
    msg = queue.get()
    writer.pub("test_reply", b'{"website_app":' + msg.body + b'}')
    msg.finish()


r = nsq.Reader(message_handler=process_message,
               nsqd_tcp_addresses=["dev.turing-ws.com:4150"],
               topic='test', channel='test', max_in_flight=9)

writer = nsq.Writer(['dev.turing-ws.com:4150'])

ta = tornado.ioloop

la = threading.Thread(target=ta.IOLoop.current().start)

la.start()
# GOProxy=https://goproxy.io
