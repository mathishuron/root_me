import socket
import re
import math

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("challenge01.root-me.org", 52002))
text = client_socket.recv(1024)
text = text.decode('ISO-8859-1')
numbers = re.findall(r'\d+', text)
print(text)
print(numbers)

result = math.sqrt(int(numbers[1])) * int(numbers[2])
result = '{:.2f}'.format(result)
result = str(result)
result += '\n'
print(result)
result = bytes(result, 'utf-8')
client_socket.sendall(result)
print("Sent")
text2 = client_socket.recv(1024)
text2 = text2.decode('ISO-8859-1')
print(text2)
