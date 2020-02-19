'''
    Write a python server program that
        0. initialized a socket connection on localhost and port 10000
        1. accepts a connection from a  client
        2. receives a "Hi <name>" message from the client
        3. generates a random numbers and keeps it a secret
        4. sends a message "READY" to the client
        5. waits for the client to send a guess
        6. checks if the number is
            6.1 equal to the secret then it should send a message "Correct! <name> took X attempts to guess the secret"
            6.2 send a message "HIGH" if the guess is greater than the secret
            6.3 send a message "LOW" if the guess is lower than the secrent
        7. closes the client connection and waits for the next one
'''
import socket                
from random import randint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 10004             
s.bind(('',port))           
s.listen(5)      
randnum = randint(0,50)
guesses = 0
name = ""
while True:
	connec, addr = s.accept()		
	while True:
		data = connec.recv(1024).decode()
		print("Input Recieved : "+data)
		if(data.find('Hi') != -1):
			name = data.split(" ")
			connec.sendall("READY".encode())
		else:
			guesses = guesses+1
			if(int(data) == randnum):
				connec.sendall(("Correct! "+name[1]+" no of guesses "+str(guesses)).encode())
				connec.close()
				break
			if(int(data)>randnum):
				connec.sendall("HIGH".encode())
			if(int(data)<randnum):
				connec .sendall("LOW".encode())
		       