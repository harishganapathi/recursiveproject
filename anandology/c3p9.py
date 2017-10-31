import re
import sys
numb = sys.argv[1]
regobj= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result =regobj.search(numb)
if result != True:
	print('it is a valid number')
else:
	print('not a valid number')


