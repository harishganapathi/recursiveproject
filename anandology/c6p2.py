numb = [12, 35, 87, 26, 9, 28, 7]
def bubble_sort(numb):
	for i in range(len(numb)-1):
		for j in range(i,len(numb)):
			if numb[i]>numb[j]:
				swap = numb[i]
				numb[i] = numb[j]
				numb[j] = swap

	return numb
print(bubble_sort(numb))

