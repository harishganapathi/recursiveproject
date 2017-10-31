inp = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}

def flat_dict(inp,result=None):
	if result is None:
		result ={}
	for x in inp:
		y = inp[x]
		if isinstance(y,dict):
			new={}
			for z in y:
				new[str(x)+'.'+str(z)]=y[z]
			flat_dict(new,result)
		else:
			result[x] = y
	return result
print(flat_dict(inp))
