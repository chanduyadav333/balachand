import socket

import json
import threading

def main():
    servers_theards()


def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)

    return config

a=len(read_config('config_file.json')['servers'])
def fun_infof(i):
    config = read_config('config_file.json')

    server_info = config['servers'][i]

    server_ip = server_info['ip']

    server_port = server_info['port']

    max_buffer_size = config['max_buffer_size']

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((server_ip, server_port))

    server_socket.listen(5)

    print(f"Server{i+1} listening on {server_ip}:{server_port}")

    while True:

        client_socket, client_address = server_socket.accept()

        print(f"Connection established with {client_address}")

        try:

            data = client_socket.recv(max_buffer_size).decode()

            print("received from client to server",i+1,":", data)

            if data == 'exit':
                print("Client sent 'exit', so client connection is closed. ")

                break

            response = f" Hcl server received: {data}"

            client_socket.send(response.encode())

        except Exception as e:

            print(f"Error handling client: {e}")

        finally:

            client_socket.close()

    server_socket.close()


def servers_theards():
    threads = []
    print("number of servers",a)
    for s in range(a):
        thread = threading.Thread(target=fun_infof, args=(s,))

        threads.append(thread)

        thread.start()

    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()
