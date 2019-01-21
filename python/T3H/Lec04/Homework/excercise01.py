def doSomeThing(numbers):
	sum_numbers = 0
	mul = 1
	for x in numbers:
		sum_numbers+=x
		mul *=x
	return (sum_numbers, mul)
print (doSomeThing([1, 2, 3, 4, 5]))