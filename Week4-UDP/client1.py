# Paul Talaga
# Sept 19, 2023
# Demo for UDP messages - client

import socket

port = 5555  # anything over 1024 
ip_server = "127.0.0.1"  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	message = input("Enter a message: ")

	s.sendto(message.encode('UTF-8'), (ip_server, port) )

	print("Message sent!")

	(msg, addr) = s.recvfrom(1024)

	msg = msg.decode('UTF-8')
	print(msg)