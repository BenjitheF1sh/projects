import socket

def receive_file(save_path, host, port):
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the host and port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(1)

        print("Waiting for connections...")

        # Accept a connection from the client
        (client_socket, client_address) = server_socket.accept()
        print("Connected to:", client_address)

        # Receive the file name from the client
        file_name = client_socket.recv(1024).decode()
        # Save the received file
        with open(save_path + "\\" + file_name, "wb") as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        print("File received and saved as:", save_path + "\\" + file_name)
    except Exception as e:
        print("Error occurred:", str(e))
    finally:
        server_socket.close()

if __name__ == "__main__":
    save_path = "D:\\Programmers_club\\vscode\\projects"  # Replace with the path where you want to save the received files
    server_host = "0.0.0.0"  # Replace with the server's IP address
    server_port = 8080  # Replace with the desired port
    receive_file(save_path, server_host, server_port)