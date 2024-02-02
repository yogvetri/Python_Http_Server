#! /usr/bin/python3



import socket

HOST = "0.0.0.0"
PORT = 65535
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print(f"Connected by {addr}")
        conn.sendall("Hello, welcome to the server!".encode())
        
        while True:
            data = conn.recv(1024)
            
            received_message = data.decode()
            print(f"Received from client: {received_message}")

            if received_message.lower() == "exit":
                print("Client requested exit. Closing connection.")
                break



            # Example of server responding back to the client
            response_message = input("Enter your response: ")
            conn.sendall(response_message.encode())
            
            # You can add additional logic here for more interactive conversation
            
           


# sck = s.socket(s.AF_INET, s.SOCK_STREAM)
# sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
# sck.bind((HOST, PORT))
# sck.listen()
# while True:
# 	print("Waiting for a new connection...")
# 	conn, addr = sck.accept()
# 	print(f"Connection received from {conn}:{addr}")