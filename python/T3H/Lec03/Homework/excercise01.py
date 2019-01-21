try:
	f = open('input.txt','r')
	clauses = f.readlines()
	f.close()
	f = open('output.txt','w+')
	for x in clauses:
		f.write(x[:-1]+' ')
	f.close()
except:
	print('file not exist')