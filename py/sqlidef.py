import socket
import re

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("163.172.101.85", 42001))
while True:
    text = client_socket.recv(1024)
    text = text.decode('ISO-8859-1')
    print(text)
    string = text.split('"')[1]
    print("extracted : ", string)
    if ("'" in string):
        result = bytes("yes","utf-8")
    else:
        result = bytes("no","utf-8")
    client_socket.sendall(result)
    client_socket.sendall(bytes('\n', 'utf-8'))
    print("Sent : ", result)
