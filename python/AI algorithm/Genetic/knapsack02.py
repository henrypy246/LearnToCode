import random

class Items:
	def __init__(self, weight, value):
		self.__weight = weight
		self.__value = value
	def show(self):
		print('weight: ',self.__weight, ' value: ', self.__value)
	def setWeight(self, weight):
		self.__weight = weight;
	def getWeight(self):
		return self.__weight
	def setValue(self, value):
		self.__value = value;
	def getValue(self):
		return self.__value

def readFile(fileName):
	file = open(fileName,"r")
	# print(file.readlines().split("\n"))
	a = []
	for line in file:
		a.append(line)
	print(a)

readFile("test.txt")
a = Items(2,3)
a.show()
	