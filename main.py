import json


class File:

    def __init__(self, name, content, protected=False):

        self.name = name
        self.content = content
        self.protected = protected


class User:

    def __init__(self, username, password, role):

        self.username = username
        self.password = password
        self.role = role


class Server:

    def __init__(self, ip, users, files):

        self.ip = ip
        self.users = users
        self.files = files



    def show_files(self):

        for file_name in self.files:
            print(file_name)



    def read_file(self, filename):

        if filename in self.files:
            file = self.files[filename]

            if file.protected:
                if current_user.role != "admin":

                    print("ADMIN ACCESS REQUIRED")
                    return
            
            print(file.content)
            
        else:
            print("File not found")

servers = [
    
    Server(
        "192.168.0.44",
        
        [
            User(
                "admin",
                "qwerty",
                "admin"
            ),
            
            User(
                "guest",
                "1234",
                "guest"
            )

        ],

        {
            "notes.txt": File(
                "notes.txt",
                "change password before friday"
            ),

            "warning.log": File(
                "warning.log",
                "DO NOT OPEN NODE-3"
            ),

            "admin.log": File(
                "admin.log",
                "TOP SECRET DATA",
                True
            )
        }
    ),

    Server(
        "192.168.0.23",
        "admin",

        {
            "mail.txt": File(
                "mail.txt",
                "meeting tomorrow"
            ),
        }
    )

]

current_server = None
logged_in = False
current_user = None



def show_help():

    print("Available commands:")
    print("     help")
    print("     scan")
    print("     connect <ip>")
    print("     ls")
    print("     cat <file>")
    print("     status")
    print("     login <user> <password>")
    print("     save <name>")
    print("     exit")



def scan():

    print("Scanning...\n")
    for server in servers:
        print(f"Found server: {server.ip}")



def connect(ip):

    global current_server
    global logged_in

    for server in servers:
        if server.ip == ip:

            current_server = server
            logged_in = False

            print(f"Connected to {ip}")
            print("Password required")
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
    
    if not logged_in:
        print("Access denied")
        return
    
    current_server.show_files()



def cat(filename):

    if current_server is None:
        print("Not connected")
        return
    
    if not logged_in:
        print("Access denied")
        return
    
    current_server.read_file(filename)



def login(username, password):

    global logged_in
    global current_user

    if current_server is None:
        print("Not connected")
        return
    
    for user in current_server.users:

        if user.username == username and user.password == password:

            logged_in = True
            current_user = user

            print(f"Access granted: {user.role}")
            return
        
    else:
        print("Wrong credentials")


def save_game(name):

    if current_server is None or current_user is None:
        print("Nothing to save")
        return
    
    data = {
        "server": current_server.ip,
        "user": current_user.username
    }

    with open(f"{name}.json", "w") as file:
        json.dump(data, file)

    print("Game saved")



def load_game(name):

    global current_server
    global current_user
    global logged_in

    with open(f"{name}.json", "r") as file:
        data = json.load(file)

    server_ip = data["server"]
    username = data["user"]

    for server in servers:

        if server.ip == server_ip:

            current_server = server
            for user in current_server.users:

                if user.username == username:

                    current_user = user
                    logged_in = True
                    print("Game loaded")
                    return




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

    elif action == "login":

        if len(parts) < 3:
            print("Usage: login <password>")

        else:
            username = parts[1]
            password = parts[2]
            login(username, password)

    elif action == "save":
        if len(parts) < 2:
            print("Usage: save <name>")

        name = parts[1]
        save_game(name)

    elif action == "load":
        if len(parts) < 2:
            print("Usage: load <name>")

        name = parts[1]
        load_game(name)

    elif action == "exit":
        break

    else:
        print("Unknown command. Use 'help'")

