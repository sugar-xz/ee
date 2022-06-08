import nsq


def handler(message):
    print(message)
    print(message.body)
    return True


r = nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['dev.turing-ws.com:4150'], topic='app__website',
               channel='app', lookupd_poll_interval=15)

nsq.run()  # tornado.ioloop.IOLoop.instance().start()
