
def randomWords(first,word = "hi", other=None):
	print(first, " is first")
	print(word, " is the word")
	if other:
		print("other given ", other)
	print()


randomWords("Mary")
randomWords("bob")
randomWords("Bill", "Ringo", "Star")

randomWords("Paul", other="something")



