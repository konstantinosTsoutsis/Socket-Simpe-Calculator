from struct import *
import socket 
import binascii

#Host IP to send to.
serverIP = '127.0.0.1'
#Port to send to
serverPort = 1000

#create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect
clientSocket.connect((serverIP, serverPort))

#user input numbers
number1 = input("enter number 1 : \n")
number1 = bytes(number1 , "utf-8")
number2 = input("enter number 2 : \n")
number2 = bytes(number2 , "utf-8")
#user input the arithmetic symbol
arithmeticSymbol = input("enter the arithmetic symbol :\nfor sum type '+'\nfor Difference type '-'\nfor Product type '*'\nfor Fraction type '/'\n")
arithmeticSymbol = bytes(arithmeticSymbol , "utf-8")

#send the numbers to server
clientSocket.send(number1)
clientSocket.send(number2)
#send the arithmetic symbol
clientSocket.send(arithmeticSymbol)

sum = clientSocket.recv(1024)
# decode to unicode string 
strings = sum.decode('utf8')
#get the num
num = float(strings)
print("the sum is : " , num)





