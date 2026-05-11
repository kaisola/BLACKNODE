print("BLACKNODE TERMINAL")


current_server = None

servers = [
    {
        "ip": "192.168.0.44",
        "password": "qwerty",

        "files": {
            "notes.txt": "change password before friday",

            "warning.log": "DO NOT OPEN NODE-3"
        }
    },

    {
        "ip": "192.168.0.23",
        "password": "admin"
    },

    {
        "ip": "192.168.0.123",
        "password": "helloworld"
    }

]




def show_help():

    print("Available commands:")
    print("scan")
    print("connect")
    print("ls")
    print("cat")

def scan():

    print("Scanning...")
    for server in servers:
        print(f"Found server: {server["ip"]}")

def connect(ip):

    global current_server

    for server in servers:
        if server["ip"] == ip:

            current_server = server

            print(f"Connected to {ip}")
            return
        
    print("Server not found")

def status():

    if current_server:
        print(current_server["ip"])
    else:
        print("Not connected")

def ls():

    if current_server is None:
        print("Not connected")
        return
    
    files = current_server["files"]

    for file_name in files:
        print(file_name)

def cat(filename):

    if current_server:
        print(current_server["ip"])
    else:
        print("Not connected")

    files = current_server["files"]

    if filename in files:
        print(files[filename])
    else:
        print("File not found")


while True:
    command = input("> ")
    parts = command.split()
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

    elif action == "exit":
        break

    else:
        print("Unknown command. Use 'help'")

