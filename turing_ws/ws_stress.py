# coding=utf-8
import json
import asyncio
import threading
import websockets
import multiprocessing
from threadpool import ThreadPool, makeRequests


class WSStress(object):
    def __init__(self, url, messages, processes=1, threads=1, headers=None):
        self.url = url
        self.messages = messages
        self.headers = headers

        self.processes = processes if isinstance(processes, int) else int(processes)
        self.threads = threads if isinstance(threads, int) else int(threads)

        self.start_num = 0
        self.err_count = 0

    async def stress_connect(self, url, msg, headers=None, sleep=1):
        message = msg if isinstance(msg, dict) else msg[0] if isinstance(msg, list) else str(msg)
        message = json.dumps(message).encode('utf-8')
        headers = None if headers in ["", {}, {'': ''}] else headers
        sleep = sleep if isinstance(sleep, int) else int(sleep)
        try:
            async with websockets.connect(url, extra_headers=headers) as websocket:
                self.start_num = self.start_num + 1

                async def con():
                    while True:
                        await websocket.send(message)
                        print("> {}".format(message))
                        data = await websocket.recv()
                        print("< {}".format(data))
                        if sleep > 0:
                            await asyncio.sleep(sleep)

                t = threading.Thread(target=(await con()))
                t.start()
        except Exception as e:
            print('Connect error:  %s' % e)
            self.err_count += 1

    def start(self, num):
        num += 1
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.stress_connect(self.url, self.messages, self.headers))

    def thread_web_socket(self):
        # 线程池
        pool_list = ThreadPool(self.threads)
        num = list()
        # 设置开启线程的数量
        for ir in range(self.threads):
            num.append(ir)
        requests = makeRequests(self.start, num)
        [pool_list.putRequest(req) for req in requests]
        pool_list.wait()

    def run(self):
        # 进程池
        pool = multiprocessing.Pool(processes=self.processes)
        # 设置开启进程的数量
        for i in range(self.processes):
            import time
            time.sleep(2)
            pool.apply_async(self.thread_web_socket)
        pool.close()
        pool.join()

        print('Strated count:  %s' % self.start_num)
        if int(self.err_count) != 0:
            print('Error count:  %s' % self.err_count)

if __name__ == "__main__":
    WS_URL = "ws://dev.turing-ws.com:8081/app/"
    token_header = {
        "Cookie": "jwt=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTQyMjUzNjEsIm9yaWdfaWF0IjoxNjEzNjIwNTYxLCJyb2xlIjoiY3VzdG9tZXIiLCJ1c2VyX2lkIjo1MCwidXNlcm5hbWUiOiJ3YW5kYUB0dXJpbmd2aWRlby5uZXQiLCJ1dWlkIjoiMjFiOTU3NjctM2NlYy00YTc1LWI0YjctZjQ3MzE2ODA5OGQwIn0.Ul4quxBIq2-mW_8vhIIVWr0NJ-kMCXiR-X7lhqwMJg2rgVy3EQ9tKWTQJFMh3gMYmfTM07LRnzsRoIAuCX8dZg;path=/;domain=.turing-ws.com;haha=123"}
    message = {
        "id": "abc",
        "act": "robot.relocalize",
        "arg": {"robot_id": "robot_test_10001", "scanning": "false",
                "pose": {"x": 2.430016077120822, "y": 1.555321336760925, "theta": -1.605265427794405}}
    }
    WSStress(WS_URL, message, processes=2, headers=token_header).run()
