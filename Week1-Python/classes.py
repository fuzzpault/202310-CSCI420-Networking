class Dog:
	def __init__(self):
		self.data = {}


	def setParamter(self, name, value):
		self.data[name] = value

	def print(self):
		for k in self.data.keys():
			print(f"{k}: {self.data[k]} ", end='')
		print()
	def __str__(self):
		self.print()

a = Dog()
a.setParamter("name","Godzilla")
a.setParamter("color","black")
a.print()

b = Dog()
b.setParamter("name","Rat")
b.setParamter("color","brown")
b.setParamter(5,55)
b.setParamter("parent",a)
b.print()