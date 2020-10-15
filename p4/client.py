import socket
s=socket.socket()
port=12346

s.connect(('',port))

while True:
	data=s.recv(1024)
	print("from server-", data)


	d=raw_input("enter you message")
	s.send(d)

s.close()