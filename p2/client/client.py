import socket
s=socket.socket()
port=12346
s.connect(('127.0.0.1',port))
filename=raw_input('enter filename:')
s.send(filename)

while True:
	print("receiving data..")
	data=s.recv(2014)
	print(repr(data))
	if not data:
		break

print("read everything!")
s.close()
print("conn closed!!")
