from struct import *
import socket
import binascii

#Host IP to listen to. If '' then all IPs in this interface
serverIP = '127.0.0.1'
#Port to listen to
serverPort = 1000
close = False
#create server socker
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket :
    #Bind the socket
    serverSocket.bind((serverIP, serverPort))
    print ("The server is ready to receive at port", str(serverPort))
    serverSocket.listen()
    while not close:
        conn, addr = serverSocket.accept()

        #print the info 
        print("Connected by:", addr)
        print("Server Socket port: ", conn.getsockname())
        print("Client Socket port: ", conn.getpeername())
        #recive the 2 numbers as bytes
        number1 = conn.recv(1024)
        number2 = conn.recv(1024)
        #recive the arithmetic symbol
        arithmeticSymbol = conn.recv(1024)
        #convert bytes to string
        number1 = number1.decode("utf-8")
        number2 = number2.decode("utf-8")
        arithmeticSymbol = arithmeticSymbol.decode("utf-8")
        #convert string to int

        number1 = float(number1)
        number2 = float(number2)
        if arithmeticSymbol == "+" :
            sum = number1 + number2        
        elif arithmeticSymbol == "-" :
            sum = number1 - number2
        elif arithmeticSymbol == "*" :
            sum = number1 * number2
        elif arithmeticSymbol == "/" :
            if number2 == 0 : 
                sum = str(sum)
                sum = "error . you cant divine a number with 0"
            else :
                sum = number1 / number2
        else :
            print("arithmetic symbol dont found")
        if (number1 >= 0 and  number1 <= 30000) and  (number2 >= 0 and  number2 <= 30000):
            #convert sum to string and then encode to bytes
            #send sum to client
            sum = str(sum)
            conn.send(str(sum).encode("utf-8"))        
            conn.close()
        else :
            sum = "error . must type a number between 0 and 3000"
            conn.send(str(sum).encode("utf-8"))        
            conn.close()
                
                


              
        

        
        
        
        
        
        
