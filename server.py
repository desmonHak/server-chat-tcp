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

def server(host='127.0.0.1', port=8000, buffer=1024):
    try:
        s = socket.socket()
        s.bind((str(host), int(port)))
        s.listen(1)
        addr, ip = s.accept()
        while True:
            _send(addr)
            _recv(addr, int(buffer))
    finally:
        s.close()


if __name__ == "__main__":
    while True:
        try:
            server(port=sys.argv[1])
        except IndexError:
            print("introduce el puerto por el que abrir el server\nserver.py 80 por ejemplo\nsinno retornara el puerto 8000")
            break