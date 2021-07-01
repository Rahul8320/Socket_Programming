#!/usr/bin/env python3
import socket
import sys
from termcolor import cprint,colored

try:
    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created!")
    s.bind((HOST, PORT))
    print("bind successful!")
    s.listen(3)
    cprint (f'Server is listening at port : {PORT}','green',attrs=['bold'])
    conn, addr = s.accept()
    cprint (f"Connection established! | IP: {addr[0]} | Port: {addr[1]}",'magenta',attrs=['bold'])

    while True:
        cprint("Receiving data ....",'yellow')
        data = str(conn.recv(4096),'utf-8')
        data = data.rstrip()
        tokens = data.split(' ')
        cprint (f"Operands received: {tokens}",'blue',attrs=['bold'])
        op = str(conn.recv(1024),"utf-8")
        cprint (f"Operator received: {op}",'blue',attrs=['bold'])
        res = int(tokens[0])
        length = len(tokens)
        for i in range(1,length):
            k = int(tokens[i])
            if(op =='+'):
                res += k
            elif op == '-':
                res -= k
            elif op == '*':
                res *= k
            elif op == '/':
                res /= k
        
        cprint("Sending data ....",'yellow')
        conn.send(str.encode(str(res)))
        cprint("Connection closed",'red',attrs=['bold'])
        conn.close()
        break
    cprint("Server closed",'red',attrs=['bold'])
    s.close() 
    
except socket.error as msg:
    cprint(f"Error : {str(msg)}",'red')
    s.close()
