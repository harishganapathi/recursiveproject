import sys
import urllib.request
#import file
link = sys.argv[1]
urlsplit = link.split("/")
filename = urlsplit[len(urlsplit)-1]
if filename[-5 :len(filename)] == '.html':
	res = urllib.request.urlopen(link)
	file = open(filename,'wb')
	file.write(res.read())
	file.close()
else:
	res = urllib.request.urlopen(link)
	file = open('index.html','wb')
	file.write(res.read())
	file.close()


