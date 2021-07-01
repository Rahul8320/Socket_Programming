import socket

host = ""
port = 8350
s = socket.socket()
print("[+] socket created successfully")
s.connect((host, port))
print("[+] Client connected at port: ",port)

f = open("music.mp4",'rb')
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