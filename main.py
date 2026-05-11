print("BLACKNODE TERMINAL")


servers = [
    {
        "ip": "192.168.0.44",
        "password": "qwerty"
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

def scan():
    print("Scanning...")
    for server in servers:
        print(f"Found server: {server["ip"]}")

def connect(ip):

    for server in servers:
        if server["ip"] == ip:
            print(f"Connected to {ip}")
            return
        
    print("Server not found")




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

    elif action == "exit":
        break

    else:
        print("Unknown command")

