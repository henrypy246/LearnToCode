# viet chuong trinh nhan dau vao la mot cau, dem so chu cai trong cau va so chu trong cau do:
def count_char_and_word(clause):
	if isinstance(clause, str):
		# tach cau thanh cac chu roi chuyen vao mot list
		words = clause.split()
		# dem so chu trong list
		numberword = len(words)
		# dem so chu cai trong cau khong tinh so
		alphabets = 0
		chars=0
		for i in range(len(clause)):
			if clause[i].isalpha(): alphabets+=1
			if clause[i].isalnum(): chars+=1
		return (words, alphabets, chars)
	else:
		return "the input is not a string"
def count_word_upper_lower(clause):
	if isinstance(clause,str):
		words = clause.split()
		uppers_word = 0
		lower_word = 0
		for x in words:
			if x.isupper(): uppers_word+=1
			if x.islower(): lower_word+=1
		return (uppers_word, lower_word)