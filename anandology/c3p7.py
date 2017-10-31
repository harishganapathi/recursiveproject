import re
def make_slug(inp):
	old = re.compile(r'^W+?|\W+|\W+$')
	new = old.sub('-',inp)
	print(new)
make_slug('---hello ---world-- ')
