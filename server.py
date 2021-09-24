import socket


class Server:
    def __init__(self, address='', port=9090):
        self.address = address
        self.port = port
        self.setup()
    def setup(self):
        self.sock = socket.socket()
        self.sock.bind((self.address, self.port))
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connected:', self.addr)
    def run(self):
        while True:
            try:
                self.data = self.conn.recv(1024)
                if self.data == b"stop":
                    self.stop()
                self.conn.send(self.data.upper())
            except ConnectionResetError:
                self.setup()
    def stop(self):
        self.conn.close()

if __name__ == "__main__":
    server = Server()
    server.run()