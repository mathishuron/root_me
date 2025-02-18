import socket
import re

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("challenge01.root-me.org", 52021))
text = client_socket.recv(1024)
text = text.decode('ISO-8859-1')
string = text.split("'")[1]
print(text)
print(string)
liste = list(string)

for i in range(len(liste)):
    if (97 <= ord(liste[i]) <= 122):
        letter = ((ord(liste[i]) - 97) + 13) % 26 + 97
        liste[i] = chr(letter)
    if (65 <= ord(liste[i]) <= 90):
        letter = ((ord(liste[i]) - 65) + 13) % 26 + 65
        liste[i] = chr(letter)

string = ''.join(liste)
print(string)
client_socket.sendall(bytes(string, 'utf-8'))
client_socket.sendall(bytes('\n', 'utf-8'))
print("Sent")
text2 = client_socket.recv(1024)
text2 = text2.decode('ISO-8859-1')
print(text2)
