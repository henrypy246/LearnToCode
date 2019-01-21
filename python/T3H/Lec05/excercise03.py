import locale
locale.setlocale(locale.LC_ALL, "en_US.utf8")
def sort_words(sequences):
	if not sequences:
		return sequences
	li = sequences.split(',')
	li.sort(key=locale.strxfrm)
	print(','.join(li))
	return ','.join(li)
sort_words('without,hello,bag,world')