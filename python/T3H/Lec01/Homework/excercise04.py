def doSomeThing():
	while True:
		a = input('Enter a number: ')
		if (int(float(a)))**2 == (float(a))**2: break
	a = int(float(a))
	if a < 0 : return a*(-1)
	return a**3