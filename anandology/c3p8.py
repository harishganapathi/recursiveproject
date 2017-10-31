import urllib.request
import re
import sys
page = sys.argv[1]
name = page[len(page)-1]
res = urllib.request.urlopen(page)
files = open(name).read()
fill = re.findall(r'<a.*?>(.+?)</a>',files)
print(str(len(fill))+"is the number of links present in this page")



