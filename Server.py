import socket
from time import sleep
from binascii import hexlify
PORT = 12345
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", PORT))
message = "this is my private message to you " + "finish"
def convert_to_binary(str):
    res=''
    global i
    for i in str:
        binary = format(ord(i), '08b')
        res += binary
    return res

binary_message = convert_to_binary(message)
socket.listen(0)
c, addr = socket.accept()

msg = "M"
count = 0
while (count < len(binary_message)):
        c.send(msg.encode())
        if (binary_message[count] == "0"):
            sleep(0.01)
        else:
            sleep(0.08)
        count += 1

c.send("finish".encode())
c.close()

