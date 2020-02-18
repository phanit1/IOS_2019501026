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
        data = data.decode()
        data = int(data)
        if not data:
            break
        print("Data from connected user " + str(i) +" : " + str(data))
        if data < rnum:
            connec.send("Your guess is lesser than the random number!".encode())
        if data > rnum:
            connec.send("Your guess is greater than the random number!".encode())
        if data == rnum:
            connec.send(("Yay! You guessed it in " + str(guesses) +" guesses").encode())
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