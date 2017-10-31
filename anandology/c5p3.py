import os,sys
direc = sys.argv[1]
for dirpath,dirs,files  in os.walk(direc):
	print(dirpath)
	#print(dirs)
	#print(files)

