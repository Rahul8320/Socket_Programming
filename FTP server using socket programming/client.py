import socket

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
    f = open("download.mkv",'wb')
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
