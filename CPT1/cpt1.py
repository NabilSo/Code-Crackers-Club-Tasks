def most(arr):
	num = {}
	count = 0
	j=0
	for i in arr:
			if i in num:
				num[i] += 1
			else:
				num[i] = 1
	maxx = 0
	numax = None

	for k in num:
		if num[k] > maxx:
			maxx = num[k]
			numax = k
	return numax

arr = [1, 3, 2, 2,2, 4, 3, 5, 2, 1, 3]
print("Most frequent element:", most(arr))



