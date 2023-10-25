# Paul Talaga
# Oct 24, 2023
# Demo for TCP - Multi-threaded so it can print message from the server
# and allow the user to send.

import socket, threading, sys

server_ip = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listenThread():
	global s
	while True:
		msg = s.recv(1024)
		if len(msg) == 0:
			sys.exit(1)
		msg = msg.decode('UTF-8')
		print(msg)

s.connect( (server_ip, port))
print("Server connected")
thread = threading.Thread(target=listenThread).start()
while True:
	message = input("What to send?")
	s.sendall(message.encode('ASCII'))
s.close()