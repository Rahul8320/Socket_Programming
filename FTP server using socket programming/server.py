import socket
import threading
import sys

host = ""
port = 8350
s = socket.socket()
print("[+] Socket created successfully")
s.bind((host, port))
print("[*] Bind successful")
s.listen(5)
print("[*] Server is listening on port: ",port)
print("[*] Default timeout 30 sec.")
s.settimeout(30)

try:
    def download_client(conn):
        f = open('video.mkv','rb')
        l = f.read(1024)
        while(l):
            conn.send(l)
            l = f.read(1024)
            if len(l) == 0:
                print("[*] File Download successful")
                break
        f.close()
        conn.close()
        
    def upload_client(conn):
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
        
    def handel_client(conn):
        conn.send(str("What u want to do (U/D)? \n1.Upload(U) file to server.\n2.Download(D) file from server.").encode())
        msg=conn.recv(1024).decode()
        print("[*] "+str(msg))
        if msg[0] == 'D':
            client_handler = threading.Thread(target=download_client,args=(conn,))
            client_handler.start()
            
        elif msg[0] == 'U':
            client_handler = threading.Thread(target=upload_client,args=(conn,))
            client_handler.start()
            
        else:
            print("[-] Socket closed successfully")
            s.close()
            sys.exit()

    while True:
        conn,addr = s.accept()
        print("[+] Connection established! | IP: "+addr[0]+" | Port: "+str(addr[1]))
        client_handler = threading.Thread(target=handel_client,args=(conn,))
        client_handler.start()
        

    client_handler.join()
    print("[-] Socket closed successfully")
    s.close()

except socket.error as msg:
    print("[*] Error: "+ str(msg))
    print("[*] Server closed")
    s.close()