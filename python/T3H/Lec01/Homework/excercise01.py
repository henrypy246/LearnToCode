# declare a list with values have type of int
l = [1, 4, 2, 5, 8, 0, 9, 6, 3, 7]

# create a list is copy of L
l_copy = l[:]

# sort descending list l_copy

l_copy.sort(reverse = True)

# find the smallest item in l

min_value = min(l) 

# find the largest item in l

max_value = max(l)

# tim phan tu trung binh cua list : khong hieu dinh nghia phan tu trung binh
# => get the item in middel of the sorted list
lenght = len(l)

middel = l_copy[int((lenght-1)/2)]

# get items have index between 3 from 7
l_3_7 = l[2:8] 

# get the items is odd

odd_list = [n for n in l if n % 2 ==1]
 