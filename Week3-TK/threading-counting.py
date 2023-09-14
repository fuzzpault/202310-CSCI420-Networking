import threading
import time

counter = 0

lock = threading.Lock()

def doStuff(name):
	global counter
	global lock
	mysum = 0
	for i in range(10000000):
		mysum += 1
		
		#time.sleep(0.1)
	lock.acquire()
	counter += mysum
	lock.release()

thread_list = []
for i in range(10):
	t1 = threading.Thread(target=doStuff, args=[i])
	t1.start()
	thread_list.append(t1)

print("All threads started!")

for i in range(10):
	thread_list[i].join()
	#print(f"Thread {i} done!")
	print("Thread", i, "Done")

print(counter)
