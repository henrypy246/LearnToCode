def doSomeThing(clause):
	if isinstance(clause, str):
		alphabets = 0
		numbers = 0
		uppers = 0
		lowers = 0
		for i in range(len(clause)):
			if clause[i].isdigit(): numbers+=1
			else:
				if clause[i].isalpha(): 
					alphabets+=1
					if clause[i].isupper(): uppers +=1
					else:lowers+=1
		chars = list(clause)
		while '@' in clause or '#' in chars:
			if '@' in chars:
				chars.remove('@')
			elif '#' in chars:
				chars.remove('#')
			else: break
		clause = ''.join(chars)
		return (alphabets, numbers, uppers, lowers, clause)
print(doSomeThing('#as jgh dk ha sd@ 12 ass7a1 f F HAKID 71Ha@ka #'))
