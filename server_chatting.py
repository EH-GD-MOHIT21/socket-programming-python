import socket
from time import sleep
grpsize=int(input("Enter grp size:->"))
s = socket.socket()
s.bind((socket.gethostbyname(socket.gethostname()),9999))
print("...waiting for joining...")
print("...Refreshing Chatting files...")
s.listen(grpsize)
s.setblocking(False)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,0)
temp=0
flag=0
addresses = []

def receive_msg(server):
    global flag
    rec_msg = False
    try:
        msg = server.recv(1024).decode()
        if msg == "mohit/d21":
            c.send(bytes("Your request for destroy server is successful","utf-8"))
            exit()
        elif(len(msg))!=0:
            print(msg)
            rec_msg = True
            file = open('data.txt','a')
            file.write(str(msg)+'\n')
            file.close()
            if rec_msg:
                for j in addresses:
                    if j!=server:
                        j.send(bytes(msg,"utf-8"))
        else:
            flag+=1
            if(flag>5000):
                print("...Server closed...")
                print("...May be Exception occured...")
                print("...Closed By Admin....")
                print("...Or Sometime it gots over...")
                exit()
    
    except Exception:
        pass
    

while True:
    try:
        c, addr = s.accept()
        temp+=1
        print(f"{temp} joined waiting for {grpsize-temp} other")
        addresses.append(c)
        c.send(bytes("...welcome to server...","utf-8"))
    except:
        pass
    for i in addresses:
        receive_msg(i)
    