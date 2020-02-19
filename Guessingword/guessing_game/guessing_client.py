'''
    Write a python client program that
        0. connects to localhost and port 10000
        1. send a "Hi <name>" message
        2. waits for the server to send the "READY" message
        3. guess a number and send to the server
        4. wait for the server to send the message
        5. Read the message and make a decision based on the following
            4.1 Close the client if the message is of the form "Correct! <name> took X attempts to guess the secret"
            4.2 Use the clue given by the server and repeat from step 3
'''
import socket

s = socket.socket()
host = socket.gethostname()
port = 12349
s.connect(("", port))
flag = True
while flag:
	msg = input()	
	print("\nClient input : "+msg)
	s.sendall(msg.encode())
	from_server = (s.recv(1024).decode())
	print("From Server : "+from_server)
	if (from_server.find('correct') != -1): 
          flag = False 
s.close()	
print("Game Completed")
