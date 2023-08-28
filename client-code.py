#import the socket library
from socket import *

#my server runs on local host on port 11500
serverName = "127.0.0.1"
serverPort = 11500

#opens a new UDP connection
clientSocket = socket(AF_INET, SOCK_DGRAM)

#anotherQ changes according to the response user provides when asked for another query,
#by default, it is set to true
anotherQ = True
while (anotherQ):
    query = str(input("nslookup: "))#name
    typeOfQuery= str(input("Type: "))#type
    clientSocket.sendto(query.encode(),(serverName, serverPort))#push name to the server's receiving port
    clientSocket.sendto(typeOfQuery.encode(),(serverName, serverPort))#push type to the server's receiving port
    serverReply, serverAddress = clientSocket.recvfrom(2048)#pull the response from the server
    print(serverReply.decode())#prints the response

    another = input("New query ? (y/n)")#prompts the user, if user responds with y, means continue, else break the loop
    if (another == "n"):
        clientSocket.sendto(str(another).encode(),(serverName, serverPort))#push the user response to the server socket
        anotherQ = False

    if (another == "y"):
        clientSocket.sendto(str(another).encode(),(serverName, serverPort))#push the user response to the server socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)#open the connection again, as it is UDP program
        
clientSocket.close()#close the connection at the end of the program


    
