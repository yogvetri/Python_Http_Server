#! /usr/bin/python3

import socket 

HOST = "0.0.0.0"
PORT = 3477


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        hi = "hello world"
        print(f"Connected by {addr}")
        conn.sendall(hi.encode())
        while True:
            data = conn.recv(1024)
        

            
            if not data :
                break
            
          
            
            conn.sendall(data)
            if data == exit:
                s.close()


# sck = s.socket(s.AF_INET, s.SOCK_STREAM)
# sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
# sck.bind((HOST, PORT))
# sck.listen()
# while True:
# 	print("Waiting for a new connection...")
# 	conn, addr = sck.accept()
# 	print(f"Connection received from {conn}:{addr}")