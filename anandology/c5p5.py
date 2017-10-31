import os,sys
folder = sys.argv[1]
dirlist = os.listdir(folder)
#print(dirlist)
count = 0
for i in dirlist:
	if i[-3:len(i)] == '.py':
		fp = open(i)
		lines = fp.readlines()
		lenline = len(lines)
		print(str(i) +" "+str(lenline))
