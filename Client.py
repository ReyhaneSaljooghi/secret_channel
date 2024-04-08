
import socket
from sys import stdout
from time import time

socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost", 12345))
data = socket.recv(1024).decode()
binary_message = ""
while not data.strip("\n").endswith("finish"):
    stdout.write(data)
    t0 = time()
    data = socket.recv(1024).decode()
    t1 = time()
    delta = round(t1 - t0, 5)
    if (delta >=0.08):
        binary_message+= "1"
    else:
        binary_message+= "0"

socket.close()

final = ""
i = 0
while i < len(binary_message):
    b = binary_message[i:i + 8]
    if len(b) < 8:
        break
    n = int(b, 2)
    final+= chr(n)
    i += 8
print("  message: " + final)