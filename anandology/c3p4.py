import os
import sys
folder = sys.argv[1]
foldtree= os.walk(folder)
for foldpath,foldirs,files in foldtree:
	path = foldpath.split('/')
	print('|'+len(path)*'--' + '[' + os.path.basename(foldpath) + ']')
	for f in files:
		print('|'  +  len(path)*'---' + str(f))


