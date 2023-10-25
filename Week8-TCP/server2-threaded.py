# Paul Talaga
# Oct 24, 2023
# Demo for TCP - Server
# Can handle multiple clients due to threading.

import socket, threading


port = 5555

def TCPWorker(sockets, client_socket):
	print("Got accept, waiting for packet")
	while True:
		
		try:
			msg = client_socket.recv(1024)
			if len(msg) == 0:
				break
			print(msg.decode("ASCII"))
			client_socket.sendall("OK".encode("ASCII"))
			for c in sockets:
				if c != client_socket:
					c.sendall(msg)
		except Exception as e:
			print(f"Got {e}")
			break
	sockets.remove(client_socket)
	print("TCP Worker died")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	sockets = []
	s.bind( ("0.0.0.0", port) )
	s.listen(0)
	print("Server waiting")
	while True:
		print("Waiting for accept")
		client_socket, addr = s.accept()
		print(f"Got accept from {addr}")
		sockets.append(client_socket)
		threading.Thread(target=TCPWorker, args=[sockets, client_socket]).start()
	s.close()