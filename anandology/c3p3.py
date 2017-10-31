import os
import sys
import time

folder = sys.argv[1]
dirlist = os.listdir(folder)
nl=[]
mydict = {}
for i in dirlist:
	splitt = i.split('.')
	nl.append(splitt)
#print(nl)
for i in range(len(nl)):
	length = len(nl[i][0])
	nl[i].append(length)
	nl[i].append(time.ctime(os.path.getmtime(str(nl[i][0]+"."+str(nl[i][1])))))

print(nl)

for i in range(len(nl)):
	print(str(nl[i][0]) + "."+str(nl[i][1])+ "\t " + str(nl[i][2]) + "\t"+str(nl[i][3]))
	



