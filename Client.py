import socket
import time

from stopwathcher import Stopwatcher


sock = socket.socket()
sock.connect(('localhost', 9090))

sw = Stopwatcher()

while True:
    d = bytes(input(), encoding="utf-8")
    sw.start()
    sock.send(d)
    print("отправил")
    data = sock.recv(2)
    sw.finish()
    print(data, sw.t)