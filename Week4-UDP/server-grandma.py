# Paul Talaga
# Sept 21, 2023
# Demo for UDP messages - server
# With room functionality that broadcasts all messages
# to all users seen so far.

import socket
import threading
import time

listen_port = 5555  # anything over 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('0.0.0.0', listen_port) )

clients = {}	# Useful so we don't double add and 
			# double send messages to anyone.

def callGrandma():
	'''  Periodicly send a message to all clients and clean out the
		clients dictionary if they don't respond within a timeout.
	'''
	global s
	msg = "ping!"
	while True:
		time.sleep(5)
		for c in clients.keys():
			s.sendto(msg.encode('UTF-8'), c )
		# See if any client hasn't responded back within 10 seconds
		del_list = [] # Build a list of clients to disconnect
		# rather than change the dictionary size on the fly
		for addr in clients.keys():
			if clients[addr] + 10 < time.time():
				del_list.append(addr)
				print(f"{addr} got removed!")
		for addr in del_list:
			del clients[addr]

thread = threading.Thread(target=callGrandma).start()

while True:
	print("Waiting for message...")
	print(clients)
	(msg, addr) = s.recvfrom(1024)
	clients[addr] = time.time()  # addr is (ip_server, port)

	# Detect special messages from the client
	msg = msg.decode('UTF-8')
	if msg == "I'mAlive!":  # From a ping above
		continue
	if msg == "NumUsers?":
		msg = f"Num users: {len(clients)}"
		s.sendto(msg.encode('UTF-8'), addr )
		continue

	
	print(f"{addr}: {msg}")

	# Change the message so the senders info is at the beginning.
	msg = f'{addr}: {msg.lower()}'

	#s.sendto(msg.encode('UTF-8'), addr )
	for c in clients.keys():
		s.sendto(msg.encode('UTF-8'), c )

