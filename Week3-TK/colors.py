from tkinter import *

master = Tk()

master.geometry("800x600")
master.configure(background="black")
colors = ['black','green','blue','purple','white']
a = 0

def changeColor(event=None):
	global master
	global colors
	global a
	master.configure(background=colors[a])
	master.after(100,changeColor)
	a += 1
	a = a % len(colors)

master.after(100,changeColor)

mainloop()