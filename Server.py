from struct import *
import socket
import binascii

#Host IP to listen to. If '' then all IPs in this interface
serverIP = '127.0.0.1'
#Port to listen to
serverPort = 1100
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
        msg = conn.recv(4)
        msg_type1 , msg_length1 = unpack('HH', msg)
        
        msg = conn.recv(msg_length1 - 4 + 1)
        msg_id , number1 ,number2 , arithmeticSymbol = unpack('IHHx1s', msg)

        arithmeticSymbol = arithmeticSymbol.decode("utf-8")
        number1 = float(number1)
        number2 = float(number2)
        
        
        response_code = 0
        sum = 0
        if (number1 >= 0 and  number1 <= 30000) and  (number2 >= 0 and  number2 <= 30000):
            if arithmeticSymbol == "+" :
              sum = number1 + number2        
            elif arithmeticSymbol == "-" :
              sum = number1 - number2
            elif arithmeticSymbol == "*" :
              sum = number1 * number2
            elif arithmeticSymbol == "/" :
                if number2 == 0 : 
                    response_code = 2   
                else :
                    sum = number1 / number2
            else :
                response_code = 3
        else :
            response_code == 1            
       
       

        msg_type1 = 1
        msg = pack('HHIf', msg_type1 , response_code, msg_id , sum)
        conn.sendall(msg)
        
        serverSocket.close()
        
                
                


              
        

        
        
        
        
        
        
