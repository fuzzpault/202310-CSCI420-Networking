# Paul Talaga
# Sept 23, 2023
# Demo for UDP messages - client
# This uses threads to listen for incoming messages from
# the server while waiting for the user to enter a
# message.

import socket
import threading
import time

port = 5555  # anything over 1024 
ip_server = "127.0.0.1"  
	# 10.34.100.43

sock_ready = False 	# Prevents the thread from listening
	# before a message is sent.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def listenThread():
	global s
	global sock_ready
	while not sock_ready:
		time.sleep(0.1)
	while True:
		(msg, addr) = s.recvfrom(1024)
		msg = msg.decode('UTF-8')
		# If a ping! message is received, reply back right now and don't
		# show it to the user.
		if msg == 'ping!':
			s.sendto("I'mAlive!".encode('UTF-8'), (ip_server, port) )
		else:
			print(msg)

thread = threading.Thread(target=listenThread).start()

while True:
	message = input("Enter a message: ")

	s.sendto(message.encode('UTF-8'), (ip_server, port) )
	sock_ready = True

	