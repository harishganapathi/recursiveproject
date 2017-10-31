import os,sys
folder = sys.argv[1]
dirlist = os.listdir(folder)
#print(dirlist)
for i in dirlist:
	count = 0
	if i[-3:len(i)] == '.py':
		print(i)
		fp = open(i)
		lines = fp.readlines()
		for i in lines:
			if i != "#" and i !="\n":
				count+=1
	print(str(count))
		#print(str(i) +" "+str(lenline))
