#!/usr/bin/env python3
import socket

try:
    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Connecting to server at port: {PORT}')
    s.connect((HOST, PORT))
    print("Connection established!")
    while True:
        print("Sending data ....")
        print("Enter 'quit' to quit from program!")
        st = input("Enter operands(with space separated) : ")
        s.send(str.encode(st))
        if st == 'quit':
             print("Socket closed")
             s.close()
             break
         
        op = input("Enter operator : ")
        s.send(str.encode(op))
        print("Receiving data ....")
        data = str(s.recv(1024),"utf-8")
        print (f'Received : {data}')
        

except socket.error as msg:
    print(f"Error : {str(msg)}")
    s.close()
