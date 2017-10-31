import os;
import sys
#for i in sys.argv
file_text = open("she.txt" , "r")
lenn = sys.argv[2]
line = file_text.readlines()
lines=  " ".join(line)
print(len(lines))
for i in range(len(lines)):
	if (i%30 == 0 and i != 0):
		print("\n")
		#print(i)
	else:
		print(lines[i],end="")



