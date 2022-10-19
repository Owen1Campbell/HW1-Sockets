# Owen Campbell
# CNT 4704 Alghamdi
from socket import *

def execute(inStr):
    i = 0
    pt1 = ""
    pt2 = ""
    while inStr[i] != '+' and inStr[i] != '-' and inStr[i] != '*' and inStr[i] != '/':
        pt1 += inStr[i]
        i += 1

    term1 = float(pt1)
    op = inStr[i]
    i += 1

    while inStr[i] != '=':
        pt2 += inStr[i]
        i += 1

    term2 = float(pt2)

    if op == '+':
        return term1 + term2
    elif op == '-':
        return term1 - term2
    elif op == '*':
        return term1 * term2
    elif op == '/':
        return term1 / term2

# portions adapted from server_tcp.py on Webcourses
# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET,SOCK_STREAM)
# Assign a port number
serverPort = 5408
# Bind the socket to server address and server port
serverSocket.bind(('',serverPort))
# Listen to at most 1 connection at a time
serverSocket.listen(1)
# Server should be up and running and listening to the incoming connections
print ('The server is ready to receive')
while True:
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # get client ip address
    hostname = gethostname()
    ip = gethostbyname(hostname)
    print("Connected with client on:", ip)
    
    # Receives the request sentence from the client
    expression = connectionSocket.recv(1024).decode()
    
    # check for exit condition
    if expression == "0/0=":
        print("Received question \"", expression, "\"; end the server program")
        connectionSocket.send("Exiting".encode())
        # Close the client connection socket
        connectionSocket.close()
        break

    # execute the math operation
    result = execute(expression)
    
    # message
    print("Received question \"", expression, "\"; send back answer ", result)

    # Send the capitalized sentence to the connection socket
    connectionSocket.send(("Result from server: " + str(result)).encode())

    # Close the client connection socket
    connectionSocket.close()
