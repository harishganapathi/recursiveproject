import os
import sys
folder = sys.argv[1]
dirlist = os.listdir(folder)
nl=[]
mydict = {}
for i in dirlist:
	splitt = i.split('.')
	nl.append(splitt)
print(nl)
for i in range(len(nl)):
	if nl[i][1] in mydict:
		mydict[nl[i][1]]  += 1
	else:
		mydict[nl[i][1]] = 1


print(mydict)


