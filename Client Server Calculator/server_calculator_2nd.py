#!/usr/bin/env python3
import socket
import threading


try:
    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created!")
    s.bind((HOST, PORT))
    print("bind successful!")
    s.listen(3)
    print (f'Server is listening at port : {PORT}')
    print("Default timeout : 10 sec")
    s.settimeout(10.0)
    
    
    def handle_client(conn):
        while True:
            print("Receiving data ....")
            data = str(conn.recv(4096),'utf-8')
            data = data.strip()
            if(data == 'quit'):
                break
            
            tokens = data.split(' ')
            print (f"Operands received: {tokens[0]} {tokens[1]}")
            op = str(conn.recv(1024),"utf-8")
            op = op.strip()
            op = op[0]
            print (f"Operator received: {op}")
            res = int(tokens[0])
            k = int(tokens[1])
            if(op =='+'):
                res += k
            elif op == '-':
                res -= k
            elif op == '*':
                res *= k
            elif op == '/':
                res /= k
            else :
                conn.send(str.encode("Unknown operator"))
                conn.close()
                return
            
            print("Sending data ....")
            conn.send(str.encode(str(res)))
            
        print("Connection closed")
        conn.close()
        
    while True:
        client, addr = s.accept()
        print (f"Connection established! | IP: {addr[0]} | Port: {addr[1]}")
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
        # break
        
    client_handler.join()
    print("Socket closed")
    client.close()
    s.close() 
    
except socket.error as msg:
    print(f"Error : {str(msg)}")
    s.close()
