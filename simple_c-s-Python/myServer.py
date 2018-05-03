import socket
sk = socket.socket()
sk.bind(('127.0.0.1',6542))
sk.listen(5)

while(True):
   conn, address = sk.accept()
   file_size = str(conn.recv(1024),encoding="utf-8")
   conn.sendall(bytes("ack", encoding="utf-8"))
   total_size =int(file_size)
   has_recv =0
   f = open('new_file.rar','wb')
   while(True):
       if total_size == has_recv:
           break
       data = conn.recv(1024)
       f.write(data)
       has_recv += len(data)
   f.close()