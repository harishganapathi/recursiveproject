import sys
import urllib.request
import re
#import file
link = sys.argv[1]
urlsplit = link.split("/")
filename = urlsplit[len(urlsplit)-1]
res = urllib.request.urlretrieve(link,filename)
files = open(filename).read()
fill = re.findall(r'>[^<]+<',files)
for i in fill:
	print(i[1:-1])
print('EOf')



