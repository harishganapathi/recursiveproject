file_name = open('she.txt','r')
lines = file_name.readlines()
new = []
for l in lines:
	new.append(l.split(" "))

sl = []

for i in range(len(new)):
	for j in range(len(new[i])):
		o = new[i].pop()
		print(o)
		new[i].insert(j,o)


print(new)
