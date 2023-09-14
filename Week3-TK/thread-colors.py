from tkinter import *
import threading
import time

master = Tk()

master.geometry("800x600")
master.configure(background="black")
colors = ['black','green','blue','purple','white']
a = 0

run = True

def changeColor(event=None):
	global master
	global colors
	global a
	global run
	while run:
		master.configure(background=colors[a])
		a += 1
		a = a % len(colors)
		time.sleep(1.0)

#master.after(100,changeColor)
t1 = threading.Thread(target=changeColor)
t1.start()

mainloop()
run = False
print("exited")