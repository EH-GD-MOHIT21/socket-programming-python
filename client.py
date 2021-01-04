import socket
name = input("Enter your name:-> ")
c = socket.socket()
c.connect((socket.gethostbyname(socket.gethostname()),9999))
print("...connected...")
print(c.recv(1024).decode())
c.setblocking(False)
temp = ""
while temp!="mohit/d21":
    temp = input("you:->")
    try:
        c.send(bytes(f"{name}:->{temp}","utf-8"))
    except:
        print("...connection leave due to some tech issues...")
        exit()
    try:
        print(c.recv(1024).decode())
    except:
        pass

c.send(bytes("mohit/d21","utf-8"))
