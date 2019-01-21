def total(a,b):
	return a+b
def total(a,b,c):
	return a+b-c
# print(total(2,3)) false
pi = 'outer pi'
# global, nonlocal
def print_pi():
	# global pi 
	pi= 'inner pi'
	def abc():
		nonlocal pi
		pi = 'jhsagdj'
		print(pi)
	abc()
	print(pi)
print_pi()
print(pi)
from math import pi
print(pi)
pi ='9asd'
print(pi)