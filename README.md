# A Rate limiter

## Aims
To write a program with client-server arch.
The Server Throws all the packages that increased the RPS.
So, after it the server MUST turns his timer and package counter to zero

## How It Actually Works
It works on async -await mechanism.
On the `main.py` you can find the  `if __name__ == '__main__':`
This invokes the server and clients.

We invoke the one server and `CLIENTS_NUM` (see all the params in `helper.py`) clients
Server works on `asyncio.DatagramProtocol`
Clients works like a simple function (it multiplied) and spawned through `asyncio.gather`

After all - server show you the output
```bash
--------------------------
Current Time 1697697969.6427567
Counter 4
Elapsed Time 0.6542303562164307
Package Has Been REJECTED
--------------------------
Current Time 1697697969.6428475
Counter 0
Elapsed Time 0.6543211936950684
Received Message: b'KC1Y81 << 2'
--------------------------
```
