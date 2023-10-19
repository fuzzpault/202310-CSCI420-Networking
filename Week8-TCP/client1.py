# Paul Talaga
# Oct 19, 2023
# Demo for TCP - Single threaded
# Required to send then receive and repeat
import socket

server_ip = "127.0.0.1"
port = 5556

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect( (server_ip, port))
	print("Server connected")
	while True:
		message = input("What to send?")
		s.sendall(message.encode('ASCII'))
		rcv = s.recv(1024)
		print(rcv.decode('ASCII'))
	s.close()