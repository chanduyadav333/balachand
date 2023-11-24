import socket
class Main:
    def con(self,message):
        host = "10.78.2.144"  # Use the server's IP address or 'localhost'
        port = 12345  # Use the same port as the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.send(message.encode("utf-8"))
        data = client_socket.recv(1024)  # Adjust the buffer size as needed
        response = data.decode("utf-8")
    def create(self):
        print("Selected: Create")
        id = input('enter id')
        name = input('enter name')
        age = input('enter the age')
        print(id, name, age)
        msg = "create," + id + "," + name + "," + age
        self.con(msg)
    def read(self):
        id=input('enter id ')
        self.con('read,'+id)
    def update(self):
        id=input('enter id for update')
        name=input('enter name')
        age=input('enter age')
        self.con('update,'+id+','+name+','+age)
    def delete(self):
        id = input('enter id to delet')
        self.con('delet,'+id)
        print("Selected: Delete")

def run():
    while True:
        print("Menu:")
        print("1: Main.create")
        print("2: Main.read")
        print("3: Main.update")
        print("4: Main.delete")
        print("Enter 'exit' to quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            Main().create()
        elif choice == "2":
            Main().read()
        elif choice == "3":
            Main().update()
        elif choice == "4":
            Main().delete()
        elif choice.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
