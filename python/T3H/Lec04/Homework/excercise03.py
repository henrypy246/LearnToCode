def canChi(year):
	can = ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']
	chi = ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mùi', 'thân', 'dậu', 'tuất', 'hợi']
	i = 0
	j = 0
	can_chi = []
	for x in range(60):
		if i == 10: i = 0
		if j == 12: j = 0
		can_chi.append((can[i][0].upper()+ can[i][1:],chi[j][0].upper()+chi[j][1:]))
		i+=1
		j+=1
	c = (year-3) %60 -1
	print (year, can_chi[c][0]+' '+can_chi[c][1])
	return (year, can_chi[c][0]+' '+can_chi[c][1])
canChi(1996)
