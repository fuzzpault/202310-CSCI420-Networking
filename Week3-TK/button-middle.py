from tkinter import *
import random
import time

master = Tk()

master.geometry("800x600")
master.configure(background="black")
colors = ['black','green','blue','purple','white','red']
a = 0
red_time = 0

def buttonClicked(event=None):
	global a
	global colors
	if colors[a] != 'red':
		print("Its not red!!!!")
		return
	elapsed = time.time() - red_time
	print(f"Elapsed: {elapsed:0.2f}")

#for x in range(10):
#	for y in range(10):
#		w = Label(master, text=f" ", font=("Helvetica", 16))
#		w.grid(row=x, column=y)

b1 = Button(master,text="Click me!")
b1.grid(column=1, row=1)
b1.bind('<Button>', buttonClicked)
b1.place(x=100, y=100)



def changeColor(event=None):
	global master
	global colors
	global a
	global red_time
	last_index = a
	while last_index == a:
		a = random.randrange(0,len(colors))
	master.configure(background=colors[a])
	master.after(1000,changeColor)
	
	if colors[a] == 'red':
		red_time = time.time()

master.after(1000,changeColor)

mainloop()