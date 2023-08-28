#import the socket library
from socket import *

serverPort = 11500

#the resource records (RR)
records = [('rohitbajaj.com', '132.157.72.21','A',300),
           ('rohitbajaj.com', 'www.theoriginalrohitbajaj.com','CNAME',300),
           ('www.rohitbajaj.com', 'www.theoriginalrohitbajaj.com','CNAME',300),
           ('www.rohitbajaj.com', '132.157.72.21','A',300),
           ('myserverforgaming.com', '121.21.32.43', 'A',200),
           ('myserverforgaming.com', 'www.myserverforgaming.com','CNAME',200),
           ('mygamingserver.com', 'www.myserverforgaming.com','CNAME',200),
           ('mygamingserver.com', '121.21.32.43','A',200)]

#response function accepts query as its parameter and process it to the pull the appropiate value from the RR
def response(query):
    temp=[]
    answer = ''
    for record in records:
        if query[0] == record[0] or query[0] == record[1]:
            temp.append(record)
    if len(temp)== 0:
        answer = f'No record found for {query[0]}'
    else:
        for i in temp:
            if query[0] in i and query[1] in i:
                if query[0] == i[0]:
                    answer = i[1]
                if query[0] == i[1]:
                    answer = i[0]
                break
            else:
                answer = f'{query[1]} type record not found for {query[0]}'
    return answer

#finish valiable helps in termination of the program in case the client response with no
#to the another query prompt in the client program
finish = True
while (finish):
    print("The Server is Listening")  #A helpful prompt
    serverSocket = socket(AF_INET, SOCK_DGRAM) #opens a new UDP connection
    serverSocket.bind(('', serverPort)) #binds the port number to the socket
    queryList = [] #[name,type] => this list object is passed to the response function for processing it
    while len(queryList) !=2: #this loop terminates when both the name and type is received from the client
        query, clientAddress = serverSocket.recvfrom(2048)
        queryList.append(query.decode())
    serverSocket.sendto((response(queryList)).encode(), clientAddress) #transmits the response to the client
    finish, clientAddress = serverSocket.recvfrom(2048) #receives "y" if client wants to make another query, else "n"
    finish = finish.decode()
    if (finish == "n"):
        finish = False #if no, terminate the program

