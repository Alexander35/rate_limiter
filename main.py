import asyncio
from server import DGProtocol
from helper import DEFAULT_SERVER, DEFAULT_PORT, CLIENTS_NUM
from client import client, run


def prepare_clients():
    clients_list = [*(client(number=i) for i in range(CLIENTS_NUM))]
    return clients_list


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = loop.create_datagram_endpoint(
        DGProtocol, local_addr=(DEFAULT_SERVER, DEFAULT_PORT)
    )
    loop.run_until_complete(server)
    asyncio.run(run(prepare_clients()))
    loop.run_forever()
