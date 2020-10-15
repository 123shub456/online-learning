import socket
s=socket.socket()
port=12346
s.bind(('', port))
s.listen(5)

while True:
	c,addr=s.accept()
	print ("got connection from addr", addr)

	data=c.recv(1024)
	print("server received filename: ",repr(data))
	filename=data

	f=open(filename,'r')
	l=f.read(1024)
	while(l):
		c.send(l)
		print("sent",repr(l))
		l=f.read(1024)
	f.close()
	print("done sending")

	c.close()