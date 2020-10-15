import socket
s=socket.socket()
port=12345

s.bind(('',port))
print("port binded")

s.listen(5)
print("socket listening")

while True:
	c, addr=s.accept()
	print("got connection from", addr)

	c.send("thanks for connecting")
	c.close()
