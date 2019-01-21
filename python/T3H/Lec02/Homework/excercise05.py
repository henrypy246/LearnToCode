def convertPhoneNumber(sequence):
	head_phone_numbers = ['096', '097','098', '0162', '0163', '0164', '0165',
	 '0166', '0167', '0168', '0169']
	head_phone_numbers_state =  ['+8496', '+8497','+8498', '+84162', '+84163', '+84164', '+84165',
	 '+84166', '+84167', '+84168', '+84169']
	new_head_phone_numbers= ['096', '097','098', '032', '033', '034', '035',
	 '036', '037', '038', '039']
	new_head_phone_numbers_state = ['+8496', '+8497','+8498', '+8432', '+8433', '+8434', '+8435',
	 '+8436', '+8437', '+8438', '+8439']
	# su dung list 
	
	for x in sequence:
		if len(x) < 10 or len(x) > 13:
			continue
		else:
			if x[0] == '0' and (len(x) == 10 or len(x) ==11):
				if len(x) == 10:
					continue
				if len(x) == 11:
					try:
						i = head_phone_numbers.index(x[:4])
						temp = x
						x = new_head_phone_numbers[i] + x[4:]
						i = sequence.index(temp)
						sequence[i] = x
					except:
						continue
			elif x[:3] == '+84' and (len(x) == 13 or len(x) ==12):
				if len(x) == 12:
					continue
				if len(x) ==13:
					try:
						i = head_phone_numbers_state.index(x[:6])
						temp = x
						x = new_head_phone_numbers_state[i] + x[6:]
						i = sequence.index(temp)
						sequence[i] = x
					except:
						continue
			else: continue
	# su dung dictionary
	"""
	
	head_phone_numbers_dict = dict(zip(head_phone_numbers, new_head_phone_numbers))
	head_phone_numbers_state_dict = dict(zip(head_phone_numbers_state, new_head_phone_numbers_state))
	for x in sequence:
		if len(x) <10 or len(x) >13:
			continue
		else:
			if len(x) ==11:
				try:
					temp = x
					x = head_phone_numbers_dict[x] + x[4:]
					i = sequence.index(temp)
					sequence[i] = x
				except:
					continue
			if len(x) ==13:
				try:
					temp = x
					x = head_phone_numbers_state_dict[x] + x[6:]
					i = sequence.index(temp)
					sequence[i] = x
				except:
					continue
	"""
	return sequence

print(convertPhoneNumber(['01648519889','0964092612','+841648519889','+84964092612']))