import nsq
import tornado.ioloop
import time


def pub_message():
    msg = time.strftime('%H:%M:%S') + ' sugar-test'
    writer.pub('app__user__50', msg.encode('utf-8'), finish_pub)


def finish_pub(conn, data):
    print(data)


writer = nsq.Writer(['dev.turing-ws.com:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
