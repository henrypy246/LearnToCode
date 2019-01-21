from collections import Counter
with open('input.txt', 'r',encoding='utf-8') as f:
	clause = f.read()
	print(clause)
	words = clause.split()
	d = Counter(words)
	li =[]
	for key,value in d.items():
		li.append(str(key)+' '+str(value))
	with open('output_ex02.txt','w',encoding='utf-8') as f_out:
		f_out.write('\n'.join(li))

"""	
	with open('output_ex02.txt','w',encoding='utf-8') as f_out:
		for x in d.keys():
			f_out.write(x + ' '+str(d[x])+'\n')
"""