

class Server:

    def __init__(self, ip, password, files):
        self.ip = ip
        self.password = password
        self.files = files



    def show_files(self):

        for file_name in self.files:
            print(file_name)



    def read_file(self, filename):

        if filename in self.files:
            print(self.files[filename])
        else:
            print("File not found")

servers = [
    
    Server(
        "192.168.0.44",
        "qwerty",

        {
            "notes.txt": "change password before friday",
            "warning.log": "DO NOT OPEN NODE-3"
        }
    ),

    Server(
        "192.168.0.23",
        "admin",

        {
            "mail.txt": "meeting tomorrow"
        }
    )

]

current_server = None




def show_help():

    print("Available commands:")
    print("help")
    print("scan")
    print("connect <ip>")
    print("ls")
    print("cat <file>")
    print("status")
    print("exit")



def scan():

    print("Scanning...\n")
    for server in servers:
        print(f"Found server: {server.ip}")



def connect(ip):

    global current_server

    for server in servers:
        if server.ip == ip:

            current_server = server

            print(f"Connected to {ip}")
            return
        
    print("Server not found")



def status():

    if current_server:
        print(current_server.ip)
    else:
        print("Not connected")




def ls():

    if current_server is None:
        print("Not connected")
        return
    
    current_server.show_files()



def cat(filename):

    if current_server is None:
        print("Not connected")
        return
    
    current_server.read_file(filename)



print("BLACKNODE TERMINAL")


while True:

    command = input("> ")
    parts = command.split()

    if len(parts) == 0:
        continue

    action = parts[0]

    if action == "help":
        show_help()

    elif action == "scan":
        scan()

    elif action == "connect":

        if len(parts) < 2:
            print("Usage: connect <ip>")

        else:
            ip = parts[1]
            connect(ip)

    elif action == "ls":
        ls()

    elif action == "cat":

        if len(parts) < 2:
            print("Usage: cat <ip>")

        else:
            filename = parts[1]
            cat(filename)

    elif action == "status":
        status()

    elif action == "exit":
        break

    else:
        print("Unknown command. Use 'help'")

