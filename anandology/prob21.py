inp = """ I'm sure that the shells are seashore shells.
    So if she sells seashells on the seashore,
    The shells that she sells are seashells I'm sure.
           She sells seashells on the seashore;"""
#print(len(inp))
coni = inp.split("\n")

#print(coni)
length = []
for i in coni:
	length.append(len(i))

justlen = max(length)

for j in coni:
	print("{}".format(j).rjust(justlen-len(j)))

