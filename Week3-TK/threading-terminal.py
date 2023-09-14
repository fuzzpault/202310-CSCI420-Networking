import threading
import time

counter = 0

def doStuff(name):
	global counter
	counter += 1
	myid = counter
	for i in range(10):
		print(f"{name} {myid}: {i}")
		time.sleep(0.1)
	counter -= 1


t1 = threading.Thread(target=doStuff, args=["Bob   "])
t1.start()

t2 = threading.Thread(target=doStuff, args=["Alice"])
t2.start()

#doStuff()
print("I'm here")
time.sleep(0.2)
print("I'm down here")
