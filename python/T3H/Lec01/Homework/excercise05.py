def solveQuadratic(a, b, c):
	if a ==0:
		if b ==0:
			return 'vô nghiệm'
		else:
			return (c/b)*(-1)
	else:
		delta = b**2 - 4*a*c
		if delta < 0: return 'vô nghiệm'
		elif delta ==0: return ((-b/(2*a)), (-b/(2*a)))
		else: return (((-b + delta**0.5)/(2*a)),((-b - delta**0.5)/(2*a)))