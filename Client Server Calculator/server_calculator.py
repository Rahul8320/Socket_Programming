#!/usr/bin/env python3
import socket

try:
    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created!")
    s.bind((HOST, PORT))
    print("bind successful!")
    s.listen(3)
    print (f'Server is listening at port : {PORT}')
    conn, addr = s.accept()
    print (f"Connection established! | IP: {addr[0]} | Port: {addr[1]}")

    while True:
        print("Receiving data ....")
        data = str(conn.recv(4096),'utf-8')
        data = data.strip()
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
            break
        
        print("Sending data ....")
        conn.send(str.encode(str(res)))
        print("Connection closed")
        conn.close()
        break
    print("Socket closed")
    s.close() 
    
except socket.error as msg:
    print(f"Error : {str(msg)}")
    s.close()
