# viet ham dao nguoc chuoi 
"""
def reverse_loop(string):
	# the parameter is a string to reverse
	if not string:
		return string
	lenght = len(string)
	chars = list(string)
	j = lenght -1
	for i in range(int(lenght/2)):
		chars[i],chars[j] = chars[j],chars[i]
		j-=1
	# return string after reverse
	return ''.join(chars)
reverse_loop('hello')

def reverse_recursive(string):
	if not string:
		return string
	else:
		return reverse_recursive(string[1:]) + string[0]
print(reverse_recursive('hello'))

def reverse(string):
	print (string[::-1])
	return string[::-1]
reverse('hello')
"""
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[0]
	def size(self):
		return len(self.items)
def reverse_stack(string):
	if not string:
		return string
	else:
		stack = Stack()
		for x in string:
			stack.push(x)
		str_reverse= ''
		for i in range(len(string)):
			str_reverse += str(stack.pop())
		print (str_reverse)
		return str_reverse
reverse_stack('hello')
