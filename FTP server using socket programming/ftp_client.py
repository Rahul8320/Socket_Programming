import socket

host = ""
port = 8350
s = socket.socket()
print("[+] socket created successfully")
s.connect((host, port))
print("[+] Client connected at port: ",port)

f = open("down.mkv",'wb')
print("[+] Downloading....")
l = s.recv(1024)
while(l):
    f.write(l)
    l = s.recv(1024)
    if len(l) == 0:
        print("[*] File transferred successful")
        break
f.close()
print("[-] Socket closed successfully")
s.close()