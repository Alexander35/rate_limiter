import socket
import string
import asyncio
import random
from helper import DEFAULT_SERVER, DEFAULT_PORT, MESSAGES_NUM


def send(msg=None):
    if msg is None:
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg.encode(), (DEFAULT_SERVER, DEFAULT_PORT))


def msg_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


async def client(number: int):
    for _ in range(MESSAGES_NUM):
        send(f'{msg_generator()} << Client #{number}')


async def run(clients):
    await asyncio.gather(*clients)
