#!/usr/bin/env python3
import socket
import sys
from termcolor import cprint,colored


try:
    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cprint(f'Connecting to server at port: {PORT}','green',attrs=['bold'])
    s.connect((HOST, PORT))
    cprint("Connection established!",'green')
    cprint("Sending data ....",'yellow')
    st = input("Enter operands(with space separated) : ")
    s.send(str.encode(st))
    op = input("Enter operator : ")
    s.send(str.encode(op))
    cprint("Receiving data ....",'yellow')
    data = str(s.recv(1024),"utf-8")
    cprint (f'Received : {data}','blue',attrs=['bold'])
    cprint("Server closed",'red',attrs=['bold'])
    s.close()

except socket.error as msg:
    cprint(f"Error : {str(msg)}",'red')
    s.close()
