import socket
import json

def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def create(data, new_entry):
    data.append(new_entry)
    return data


def read(data, entry_id):
    for entry in data:
        if entry.get('id') == entry_id:
            return entry
    return None


def update(data, entry_id, updated_entry):
    for i, entry in enumerate(data):
        print(i,entry)
        if entry.get('id') == entry_id:
            data[i] = updated_entry
            return data
    return None


def delete(data, entry_id):
    for i, entry in enumerate(data):
        if entry.get('id') == entry_id:
            del data[i]
            return data
    return None


def start_server():
    host = "10.78.2.144"  # Use your server's IP address or 'localhost'
    port = 12345  # Choose an available port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Handle the connection (you can customize this part)
        handle_client(client_socket)


def handle_client(client_socket):
    with open('file.json', 'r') as json_file:
        data = json.load(json_file)
    file_path = "file.json"
    while True:
        data1 = client_socket.recv(1024)  # Adjust the buffer size as needed
        if not data1:
            break  # Break the loop if no data is received
        message = data1.decode("utf-8")
        #print(f"Received from client: {message}")
        l=list(message.split(','))
        if l[0]=='create':
            new_entry = {"id": int(l[1]), "name": l[2], "age": int(l[3])}
            data = read_json(file_path)
            data = create(data, new_entry)
            print('successfully created')
            write_json(file_path, data)
        elif l[0]=='read':
            entry_id_to_read = int(l[1])
            entry = read(data, entry_id_to_read)
            print("Read:", entry)
            print('successfully read')
        elif l[0]=='update':
            entry_id_to_update = int(l[1])
            updated_entry = {"id": l[1], "name": l[2], "age": int(l[3])}
            data = update(data, entry_id_to_update, updated_entry)
            write_json(file_path, data)
            print('successfully updated')
        else:
            entry_id_to_delete = int(l[1])
            data = delete(data, entry_id_to_delete)
            write_json(file_path, data)
            print('successfully deleted')
        # Respond back to the client (you can customize this part)
        response = "Server received your message"
        client_socket.send(response.encode("utf-8"))

    client_socket.close()


if __name__ == "__main__":
    start_server()
