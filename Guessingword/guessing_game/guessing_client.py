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

def main():

    host = '10.10.11.215'
    port = 5151

    sockobj = socket.socket()
    sockobj.connect((host, port))
    print('Hi name')
    # print("Welcome to a New Game of Guess the Number")
    message = input("Enter a number to guess: ")

    while message != 'q':

        sockobj.send(message.encode())

        data = sockobj.recv(1024)

        print("Data Received From Server: " + str(data.decode()))

        check = str(data.decode()).split(" ")

        if check[0] == "Yay!":
            print("Thanks For Playing :)")
            sockobj.close()
            return
        message = input("Enter a number to guess: ")
    sockobj.close()

if __name__ == '__main__':
        main() 