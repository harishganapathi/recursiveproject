import tablib,os,sys
srcfile = sys.argv[1]
destfile = sys.argv[2]

obje = tablib.Dataset()
length = len(open(srcfile).readlines())
fop = open(srcfile)
i=0
while i < length:
	obje.append(i,fop.readline().strip())
	i+=1

with open(destfile + '.xls' , 'wb') as fp:
	fp.write(obje.xls)


