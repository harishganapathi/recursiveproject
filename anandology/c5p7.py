import os,sys
filename = sys.argv[1]
numfiles = sys.argv[2]
fp = open(filename)
files = fp.readlines()[:]
length = len(files)
filesline  =int( length/int(numfiles))
for i in range(int(numfiles)):
	new = open(str(i)+'.txt','w')
	for j in range(filesline):
		new.write(files.pop())
fp.close()
