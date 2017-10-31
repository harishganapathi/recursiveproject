import sys
filename = sys.argv[1]
f = open(filename,'r')
for i in range(length):
	lines = f.readline()
	if len(lines)<40:
		print(f.readline())

