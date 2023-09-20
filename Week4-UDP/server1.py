# Paul Talaga
# Sept 19, 2023
# Demo for UDP messages - server

import socket

listen_port = 5555  # anything over 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('0.0.0.0', listen_port) )

while True:
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(1024)

	msg = msg.decode('UTF-8')
	print(f"{addr}: {msg}")

	msg = msg.lower() + " haha!"

	s.sendto(msg.encode('UTF-8'), addr )

