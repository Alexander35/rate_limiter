import asyncio
import time
from helper import RPS_TRASHOLD_TIME, RPS_TRASHOLD_PACKAGES_NUM


class DGProtocol(asyncio.DatagramProtocol):
    timer = 0
    counter = 0

    def __init__(self):
        super().__init__()
        self.timer = time.time()
        self.counter = 0

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        current_time = time.time()
        print('--------------------------')
        print('Current Time', current_time)
        print('Counter', self.counter)
        print('Elapsed Time', current_time - self.timer)
        if current_time - self.timer > RPS_TRASHOLD_TIME and self.counter > RPS_TRASHOLD_PACKAGES_NUM:
            print('Package Has Been REJECTED')
            self.counter = 0
            return

        print(f"Received Message: {data}")
        self.counter = self.counter + 1

