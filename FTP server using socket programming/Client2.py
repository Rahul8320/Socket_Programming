import socket
import os
import promptlib as pt

host = ""
port = 8350
s = socket.socket()
print("[+] socket created successfully")
s.connect((host, port))
print("[+] Client connected at port: ",port)

msg=s.recv(1024).decode()
print("[*] "+str(msg))
ans=input(">>>  ")
s.send(str(ans).encode())

if ans[0] == 'D':
    lst = s.recv(4096).decode()
    print(lst)
    file_name = input("Enter file name with extension >> ")
    s.send(str(file_name).encode())
    print("Select your folder >>> ")
    prom = pt.Files()
    dir = prom.dir()
    print("[*] Current dir : "+ str(dir))
    file_name = dir+'/'+file_name
    f = open(file_name,'wb')
    print("[+] Downloading....")
    l = s.recv(1024)
    while(l):
        f.write(l)
        l = s.recv(1024)
        if len(l) == 0:
            print("[*] File Download successful")
            break
    f.close()

elif ans[0] == 'U':
    print("Select your folder >>> ")
    prom = pt.Files()
    dir = prom.dir()
    print("Select your file to upload >>> ")
    file = prom.file()
    s.send(str(file).encode())
    f = open(file,'rb')
    print("[+] Uploading....")
    l = f.read(1024)
    while(l):
        s.send(l)
        l = f.read(1024)
        if len(l) == 0:
            print("[*] File upload successful")
            break
    f.close()

print("[-] Socket closed successfully")
s.close()
