import socket

def main():
	host = '10.10.11.215'
	port = 5051

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))

	s.listen(5)
	message, addr = s.accept()
	print("Connection from:  " +str(addr))

	while True:
			data = message.recv(1024).decode('ASCII')
			if not data:
				break
			print("from connected user: " + str(data))
			data = str(data).upper()
			print("sending: " + str(data))
			message.send(str(data).encode('ASCII')) 
	message.close()

if __name__ == '__main__':
	main()