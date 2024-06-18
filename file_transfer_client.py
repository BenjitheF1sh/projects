import socket

def send_file(file_path, host, port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))

        # Send the file name to the server
        file_name = file_path.split("\\")[-1]
        print(file_name)
        client_socket.send(file_name.encode())

        # Open the file and send its contents to the server
        with open(file_path, "rb") as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.sendall(data)

        print("File sent successfully.")
    
    except Exception as e:
        print("Error occurred:", str(e))
    
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"  # Replace with the server's IP address
    server_port = 8080  # Replace with the server's port
    file_path = "D:\\Programmers_club\\test_files_etc\\file_transfer.txt"  # Replace with the actual file path
    send_file(file_path, server_host, server_port)