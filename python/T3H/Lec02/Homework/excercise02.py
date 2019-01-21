def checkPassword(password):
	if isinstance(password, str):
		lenght = len(password)
		if lenght < 8 or lenght >16:
			return False
		special_characters = ['@', '*', '#', '!', '$']
		check_upper = False
		check_lower = False
		check_digit = False
		check_special_char = False
		for i in range(lenght):
			if not check_upper:
				if password[i].isupper(): check_upper = True
			if not check_lower:
				if password[i].islower(): check_lower = True
			if not check_digit:
				if password[i].isdigit(): check_digit =	True
			if not check_special_char:
				if password[i] in special_characters: check_special_char = True
			if check_upper* check_lower* check_digit*check_special_char: return True
		return bool(check_upper* check_lower* check_digit*check_special_char)

print(checkPassword("#include86H"))
