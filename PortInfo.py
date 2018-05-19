import socket
socket.setdefaulttimeout(2) #set timeout for scanning
s=socket.socket()
s.connect(("192.168.43.95",21))  #Enter ip address and port to which you want to connect.
result=s.recv(1024) #recv(1024) read next 1024 bytes on the socket
print(result)
