import urllib.request,json
url = "http://httpbin.org/get"
res = urllib.request.urlopen(url)
data = json.loads(res.read().decode())

print(data)
print(data["origin"])

