inp = [12, 35, 87, 26, 9, 28, 7]

def selection_sort(inp):
	for i in range(len(inp)):
		#for j in range(i,len(inp)):
		minval = min(inp[i:len(inp)])
		print(minval)
		swap = inp[i]
		print(swap)
		inp[i] = minval
		print(inp[i])
		inp[inp.index(minval)] = swap
	return inp
print(selection_sort(inp))


