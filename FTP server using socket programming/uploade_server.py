import socket
import threading

host = ""
port = 8350
s = socket.socket()
print("[+] Socket created successfully")
s.bind((host, port))
print("[*] Bind successful")
s.listen(3)  # 3 requests in queue if server is busy
print("[*] Server is listening on port: ",port)

def handel_client(conn):
    f = open('upload.mp4','wb')
    l = conn.recv(1024)
    while(l):
        f.write(l)
        l = conn.recv(1024)
        if len(l) == 0:
            print("[*] File Upload successful")
            break
    f.close()
    conn.close()
    
    
while True:
    conn,addr = s.accept()
    print("[+] Connection established! | IP: "+addr[0]+" | Port: "+str(addr[1]))
    client_handler = threading.Thread(target=handel_client,args=(conn,))
    client_handler.start()
    break

client_handler.join()
print("[-] Socket closed successfully")
s.close()