import random
def generatePassword():
	special_characters = ['@', '*', '#', '!', '$']
	digit = [n for n in range(10)]
	alphabets = [chr(i) for i in range(65,91)]
	lenght = random.randint(8,16)
	check_digit = False
	check_special = False
	check_lower = False
	check_upper = False
	password = ''
	special_list = special_characters + alphabets + digit + [n.lower() for n in alphabets]
	for i in range(lenght):
		if i < 4:
			password += str(random.choice(special_list))
			continue
		if not check_special:
			password += random.choice(special_characters)
			check_special = True
			continue
		if not check_upper:
			password += random.choice(alphabets)
			check_upper = True
			continue
		if not check_lower:
			password += (random.choice(alphabets)).lower()
			check_lower = True
			continue
		if not check_digit:
			password += str(random.choice(digit))
			check_digit = True
			continue
		if check_digit*check_lower*check_upper*check_special:
			password += str(random.choice(special_list))
			continue
	return password
print(generatePassword())

