def funone(n):
	return n*n

def mappit(f,a):
	ret = [f(i) for i in a]
	return ret
op = mappit(funone,[1,2,3])
print(op)

