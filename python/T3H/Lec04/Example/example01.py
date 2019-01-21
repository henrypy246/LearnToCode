from collections import defaultdict

classes = [('V',1),('VI',1),('V',2),('VI',2),('VI',3),('VII',1)]
result = defaultdict(list)
for item in classes:
	result[item[0]].append(item[1])
"""
d = dict()
for item in classes:
	if item[0] not in d.keys():
		d[item[0]]=[item[1]]
	else:
		if item[0] in d.keys():
			if item[1] not in d[item[0]]:
				d[item[0]].append(item[1])
				"""

print(result)
