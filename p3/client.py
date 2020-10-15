import socket
s=socket.socket()
port=12345
s.connect(('127.0.0.1',port))

ip_add=raw_input("Enter the ip_address:")
s.send(ip_add)

c=s.recv(1024) 
print("class=",c)
s.close()