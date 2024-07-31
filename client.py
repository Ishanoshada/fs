import socket

def receive_file(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(filename.encode())

        response = s.recv(1024)
        if response == b'ERROR: File not found':
            print("Error: File not found on the server.")
            return

        with open(f'received_{filename}', 'wb') as file:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"File '{filename}' received successfully")

if __name__ == "__main__":
    filename = 'example.txt'  # File to request from the server
    host = '127.0.0.1'  # Replace with the server's IP address
    port = 65432

    receive_file(filename, host, port)
