import socket
s=socket.socket()
port=12345

s.bind(('',port))
s.listen(5)

while True:
	c, addr=s.accept()
	print("socket connected to",addr)

	data=c.recv(1024)
	print("ip received", repr(data))
	arr=data.split('.')
	x=arr[0]
	class_type='O'
	print("class",x)
	
	x=int(x)
	if (x>1 and x<126):
		class_type='A'
	elif (x<191):
		class_type='B'
	elif (x<223):
		class_type='C'
	elif (x<239):
		class_type='D'
	elif (x<255):
		class_type='E'

	c.send(class_type)
	print("sent",class_type)
	print("everything successful")
	c.close()


