import itertools
def funp(it):
	iterable =list(it)
	return iterable[0],iterable
op = funp(iter(range(5)))
print(op)
