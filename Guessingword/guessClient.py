import socket

def main():

    host = '10.10.11.215'
    port = 5151

    sockobj = socket.socket()
    sockobj.connect((host, port))

    print("Welcome to a New Game of Guess the Number")
    message = input("Enter Your number ->")

    while message != 'q':

        sockobj.send(message.encode())

        data = sockobj.recv(1024)

        print("Data Received From Server: " + str(data.decode()))

        check = str(data.decode()).split(" ")

        if check[0] == "Yay!":
            print("Thanks For Playing :)")
            sockobj.close()
            return
        message = input("Enter Your number ->")
    sockobj.close()

if __name__ == '__main__':
        main() 