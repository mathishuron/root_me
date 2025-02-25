import socket
import re

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("163.172.101.85", 42003))
while True:
    text = client_socket.recv(1024)
    text = text.decode('ISO-8859-1')
    print(text)
    string = text.split('"')[1]
    print("extracted : ", string)
    if ("'" in string or ".." in string or "{{" in string or "passwd" in string or "shadow" in string or "/proc" in string or "/var" in string):
        result = bytes("yes","utf-8")
        client_socket.sendall(result)
        client_socket.sendall(bytes('\n', 'utf-8'))
        print("Sent : ", result)
        text2 = client_socket.recv(1024)
        text2 = text2.decode('ISO-8859-1')
        print(text2)
        ip = re.findall('[0-9]+(?:\.[0-9]+){3}', text)
        result = bytes(ip[0],"utf-8")
        client_socket.sendall(result)
        client_socket.sendall(bytes('\n', 'utf-8'))
        print("Sent : ", result)
        text3 = client_socket.recv(1024)
        text3 = text3.decode('ISO-8859-1')
        print(text3)
        my_index = string.index('=')
        payload = string[my_index + 1:-9]
        result = bytes(payload,"utf-8")
        client_socket.sendall(result)
        client_socket.sendall(bytes('\n', 'utf-8'))
        print("Sent : ", result)


    else:
        result = bytes("no","utf-8")
        client_socket.sendall(result)
        client_socket.sendall(bytes('\n', 'utf-8'))
        print("Sent : ", result)
