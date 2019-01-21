def use_magic(positions):
	if not positions:
		return positions
	else:
		magic = []
		for x in positions:
			if x[1] >= x[2]: magic.append(x[1]-x[2])
			else:
				counter = 0
				if x[1]*2 > x[2]:
					