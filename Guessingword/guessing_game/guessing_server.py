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
import threading
from random import randint

def function(sockobj, i):
    rnum = randint(0,50)
    connec, addr = sockobj.accept()
    print("Connection from: " + str(addr))
    guesses = 0
    while True:
        guesses = guesses + 1
        data = connec.recv(1024)
        connec.send('READY')
        data = data.decode()
        data = int(data)
        if not data:
            break
        print("Data from connected user " + str(i) +" : " + str(data))
        if data < rnum:
            connec.send('LOW'.encode())
        if data > rnum:
            connec.send('HIGH'.encode())
        if data == rnum:
            connec.send(("Correct! <name> took "+str(guesses) +" attempts to guess the secret ").encode())
            connec.close()
            return
def main():

    totalconnec = 10

    host = '10.10.11.215'
    port = 5151
    
    sockobj = socket.socket()
    
    sockobj.bind((host, port))
    
    sockobj.listen(1)
    threadarr = list()
    for i in range(0, totalconnec):
        thread = threading.Thread(target = function, args = (sockobj, i))
        threadarr.append(thread)
        threadarr[i].start()    
    for i in range(0, totalconnec):
        threadarr[i].join()

if __name__ == '__main__':
            main()