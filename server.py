import socket

def send_file(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Server started {host}:{port}")
        s.bind((host, port))
        s.listen(1)
        print(f"Server listening on {host}:{port}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            with open(filename, 'rb') as file:
                data = file.read(1024)
                while data:
                    conn.sendall(data)
                    data = file.read(1024)
            print("File sent successfully")

if __name__ == "__main__":
    filename = 'example.txt'  # Replace with the file you want to send
    host = '0.0.0.0'  # Listen on all interfaces
    port = 8881

    send_file(filename, host, port)
