#! /usr/bin/python3


import socket as s
from threading import Thread
import mimetypes as m


http_resp_template = """HTTP/1.1 200 OK
Connection: Keep-Alive
Content-Type: {type}
Accept-Ranges: bytes
Content-Length: {length}
Vary: Accept-Encoding
Server: Apache/2.4.41 (Ubuntu)

{body}"""

htdocs = 'htdocs'



class Create_a_Thread(Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = self
        print(f"Thread {addr[0]}:{addr[1]} started.....")

    def session(self):
        data = conn.recv(4567)
        header = data.decode().split('\n')[0]
        file = header.split(" ")[1]
        if file == "/":
            file = "index.html"
        file = "htdocs"+file
        with open(file ,'r') as files:
            body = files.read()
        conn.sendall(http_resp_template.format(type=m.guess_type(file)[0], length = len(body), body = body).encode())



host = "0.0.0.0"#configure port forwarding to get internet traffic
port = 65534

with s.socket(s.AF_INET, s.SOCK_STREAM):
    s.bind((host, port))
    s.listen()
    while True:
        print("Waiting for a new connection...")
        conn, addr = s.accept()
        print(f"Connectoin recived from {addr[0]}:{addr[1]}")
        Create_a_Thread(conn, addr).start()

    