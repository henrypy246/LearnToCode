def squareRoot(x):
	x = float(x)
	e = 0.0000000001
	g = x*2
	while(abs(x - g*g) >e):
		g = (g + x/g)/2
	return g
print(squareRoot(2))
