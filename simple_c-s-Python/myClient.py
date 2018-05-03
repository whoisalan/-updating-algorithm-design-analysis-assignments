import socket
import os
obj = socket.socket()
obj.connect(('127.0.0.1',6542))
size = os.stat("paper list.rar").st_size
obj.sendall(bytes(str(size), encoding="utf-8"))
obj.recv(1024)
with open("paper list.rar","rb") as f:
   for line in f:
       obj.sendall(line)
obj.close()