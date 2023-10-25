# Paul Talaga
# Oct 19, 2023
# Demo for TCP - Server
# Can only handle a single client at a time.
import socket


port = 5556

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind( ("0.0.0.0", port) )
	s.listen(0)
	print("Server waiting")
	while True:
		print("Waiting for accept")
		client_socket, addr = s.accept()
		print(f"Got accept from {addr}")
		while True:
			
			try:
				msg = client_socket.recv(1024)
				if len(msg) == 0:
					break
				print(msg.decode("ASCII"))
				client_socket.sendall("OK".encode("ASCII"))
			except Exception as e:
				print(f"Got {e}")
				break
	s.close()