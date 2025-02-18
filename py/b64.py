import socket
import re
import base64

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("challenge01.root-me.org", 52023))
text = client_socket.recv(1024)
text = text.decode('ISO-8859-1')
string = text.split("'")[1]
print(text)
print(string)

result = base64.b64decode(string)
print(result)
client_socket.sendall(result)
client_socket.sendall(bytes('\n', 'utf-8'))
print("Sent")
text2 = client_socket.recv(1024)
text2 = text2.decode('ISO-8859-1')
print(text2)
