from struct import *
import socket 
import binascii

#Host IP to send to.
serverIP = '127.0.0.1'
#Port to send to
serverPort = 1100
#create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect
clientSocket.connect((serverIP, serverPort))
msg_type = 0
msg_id = 35
msg_length = 13
#user input numbers
number1 = input("enter number 1 : \n")
number2 = input("enter number 2 : \n")
#user input the arithmetic symbol
arithmeticSymbol = input("enter the arithmetic symbol :\nfor sum type '+'\nfor Difference type '-'\nfor Product type '*'\nfor Fraction type '/'\n")
msg = pack('HHIHHx1s', msg_type , msg_length , msg_id ,int(number1) , int(number2) , arithmeticSymbol.encode('utf-8'))

#send
clientSocket.sendall(msg)

#receve sym from server
sum = clientSocket.recv(12)

msg_type , response_code ,msg_id , sum = unpack('2HIf', sum)

if response_code == 0 :
    print("the sum is : " , sum)
elif response_code == 1 :
    print("Number is greater than 3000") 
elif response_code == 2 :
    print("Impossible division")
elif response_code == 3 :
    print("arithmetic symbol not found")    
clientSocket.close()





