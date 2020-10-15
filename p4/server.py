import socket
s=socket.socket()
port=12346
s.bind(('',port))
s.listen(5)

while True:
	c, addr=s.accept()

	print("connection successful")
	while True:
		msg=raw_input("enter your message")
		c.send(msg)

		data=c.recv(1024)
		print("from client", data)

	c.close()