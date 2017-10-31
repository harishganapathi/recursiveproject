text_file = open("she.txt", "r")
lines = text_file.readlines()
inp = []
for i in lines:
	inp.append(i)
def reverse(inp):
	newlist = []
	for i in range(len(inp)):
		newlist.append(inp.pop())
	return newlist
op = reverse(inp)
print(op)
