inp =[1, 2, 3] ; inp2 =  ["a", "b", "c"]
a = inp
b = inp2
def zipit(a,b):
	nl = []
	for i in range(len(a)):
		for j in range(len(b)):
			if i==j:
				nl.append((a[i],b[j]))
	return nl

op = zipit(inp,inp2)
print(op)
#using list comprehension
nlw = [(a[x],b[y])for x in range(len(a)) for y in range(len(b)) if x == y ]
print(nlw)




