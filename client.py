# Owen Campbell
# CNT 4704 Alghamdi
import numbers

def isValid(inStr):
    hasOp = False
    i=1

    # must begin with number
    if inStr[0].isnumeric() == False:
            return False
        
    while i < len(inStr)-1:
        if inStr[i] == ' ':
            continue

        if inStr[i] == '+' or inStr[i] == '-' or inStr[i] == '*' or inStr[i] == '/':
            if hasOp:
                return False
            else:
                hasOp = True
                i += 1
                continue
        # check for valid numbers
        if inStr[i].isnumeric() == False:
            return False
        # increment loop
        i += 1

    # must end in '='
    if inStr[len(inStr)-1] != '=':
        return False

    # invalid if missing operator
    if hasOp == False:
        return False

    # check if expression has no second term (ex: 1+=)
    if inStr[len(inStr)-2] == '+' or inStr[len(inStr)-2] == '-' or inStr[len(inStr)-2] == '*' or inStr[len(inStr)-2] == '/':
        return False
    
    # all conditions met
    return True

# main function

#portions of socket code adapted from client_tcp.py on Webcourses
from socket import *

serverName = "eustis3.eecs.ucf.edu"
serverPort = 5408

expression = ""
while expression != "0/0=":
    expression = input("Enter an expression: ")
    # check clientside if expression meets requirements
    if isValid(expression) == True:
        # create socket and establish TCP connection only if expression is valid
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))

        # get server ip address
        hostname = gethostname()
        ip = gethostbyname(hostname)
        print("Connected with server on:", ip)

        # send input to server
        clientSocket.send(expression.encode())
        # get result from server
        result = clientSocket.recv(1024)
        print (result.decode())
        # close socket
        clientSocket.close()
    else:
        print("Input error. Re-type the math question again.")
