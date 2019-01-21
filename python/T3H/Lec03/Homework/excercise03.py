def tinhTong(number):
	sum_of_number = sum([int(x) for x in str(number)])
	if sum_of_number < 10:
		return sum_of_number
	else:
		return tinhTong(sum_of_number)
print(tinhTong(7856))