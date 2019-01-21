matrix = [[['*' for x in range(6)] for y in range(4)] for z in range(3)]
print(matrix)
"""
for z in range(len(matrix)):
	for y in range(len(matrix[0])):
		for x in range(len(matrix[0][0])):
			print(matrix[z][y][x], end=' ')
		print()
	print(' ')
"""