import socket

HOST = "localhost"  # Change this to the actual server's IP address or hostname
PORT = 65535

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        data = s.recv(5624)
        print(f"Received from server: {data.decode()}")

        if data.decode().lower() == "exit":
            print("Server requested exit. Closing connection.")
            break

        user_input = input("Enter your message: ")
        s.sendall(user_input.encode())

        if user_input.lower() == "exit":
            print("Exiting client.")
            break
