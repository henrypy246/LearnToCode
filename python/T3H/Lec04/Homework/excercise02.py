def getNumbers(sequence):
	l = sequence.split()
	numbers = []
	print(l)
	for x in l:
		try:
			value = float(x)
			value_01 = int(value)
			if value == value_01:	
				numbers.append(value_01)
			else: numbers.append(value)
		except:
			s = ''
			for i in range(len(x)):
				if x[i].isdigit() or x[i]=='.':
					s =s + x[i]
				else:
					try:
						v = float(s)
						v_01 = int(v)
						if v == v_01:
							numbers.append(v_01)
						else: numbers.append(v)
						s = ''
					except:
						s = ''
	print(numbers)
	return numbers

getNumbers( 'Em ơi có bao nhiêu, 60năm cuộc đời, -20 năm đầu, sung sướng0bao lâu32.12')