import socket
import sys

def _recv(target, buffer):
    dat = target.recv(int(buffer))
    if dat == 'exit':
        exit()
    else:
        print(dat.decode())


def _send(target):
    dat = str(input(">>: "))
    if dat == 'exit':
        target.send(dat.encode())
        exit()
    else:
        target.send(dat.encode())


def client(host='127.0.0.1', port=8000, buffer=1024):
    try:
        s = socket.socket()
        s.connect((str(host), int(port)))
        while True:
            _recv(s, int(buffer))
            _send(s)

    finally:
        s.close()


if __name__ == "__main__":
    while True:
        try:
            client(host=sys.argv[1], port=sys.argv[2])
        except IndexError:
            print("introduce el puerto por el que conectarse al server\nclient.py 127.0.0.1 80 por ejemplo\nsinno retornara el puerto 8000 por la ip 127.0.0.1")
            break
