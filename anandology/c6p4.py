inp = {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
def flat_list(inp,result = None):
	if result is None:
		result = {}

	new = {}
	for key in inp:
		val = inp[key]
		if  "." in key:
			k = key.split(".")
			i=0
			while i<len(k):
				new[k[i+1]]= val
				result[k[i]] = new	
				i+=2
		else:
			result[key] = val
	return result

print(flat_list(inp))
