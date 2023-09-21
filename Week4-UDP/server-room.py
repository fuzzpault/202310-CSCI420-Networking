# Paul Talaga
# Sept 21, 2023
# Demo for UDP messages - server
# With room functionality that broadcasts all messages
# to all users seen so far.

import socket

listen_port = 5555  # anything over 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('0.0.0.0', listen_port) )

clients = set()	# Useful so we don't double add and 
			# double send messages to anyone.

while True:
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(1024)
	clients.add(addr)
	print(clients)

	msg = msg.decode('UTF-8')
	print(f"{addr}: {msg}")

	# Change the message so the senders info is at the beginning.
	msg = f'{addr}: {msg.lower()}'

	#s.sendto(msg.encode('UTF-8'), addr )
	for c in clients:
		s.sendto(msg.encode('UTF-8'), c )

