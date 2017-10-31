import os,sys,zipfile
zipname = sys.argv[1]
print(zipname)
iterzip = sys.argv[2:]
with zipfile.ZipFile(zipname,'w') as myzip:
	for i in iterzip:
		myzip.write(i)


