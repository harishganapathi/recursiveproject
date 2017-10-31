#prob2
l = [1,2,3]
sum = 0
for i in l:
	sum = sum+i
print(sum)


#prob3
app = ""
p3i = ['hello' , 'world']
for i in p3i:
	app += str(i)

print(app)


#prob4


mul =  1
p4 = [1,2,3]
for i in p4:
	mul = i*mul
print(mul)


#prob5

def fact(n):
	if n == 1 :
		return n
	else:
		return n * fact(n-1)
print(fact(4))


#prob6
b = []
def reverse(a):

	while len(a)>=1:
		c = a.pop()
		b.append(c)
	return b

print(reverse([1,2,3]))


#prob8
def cumilative(n):
	b=[]
	mul = 1
	for i in range(len(n)):
		for j in range(i+1):
			mul = mul * n[j]
		b.append(mul)
		mul = 1
	return b

print(cumilative([1,2,3,4]))
#prob10
lis = [1, 2, 1, 3, 2, 5]
def unique(lis):
	nl = []
	for i in l:
		if l.count(i)<2:
			nl.append(i)
	return nl
print(unique(lis))

#prob 11
l = [1, 2, 1, 3, 2, 5]
def dups(l):
	nl = []
	for i in l:
		if l.count(i)>1:
			nl.append(i)
	return list(set(nl))
print(dups(l))

#prob 12
def group(lis,size):
	q = len(lis)% size
	r = int(len(lis)/size)
	no = q + r
	newlist = []
	for i in range(no):
		newlist.append([])
		for j in range(size):
			newlist[i].append(lis[j])


	return newlist

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9],3))




#prob13
li = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
def lensort(li):
	for i in range(len(li)):
		for j in range(i+1,len(li)):
			if len(li[i])>len(li[j]):
				swap = li[i]
				li[i] = li[j]
				li[j] = swap
	return li
print(lensort(li))




#prob14


def extsort(lop):
	for i in range(len(lop)):
		lop[i] = lop[i].split('.')
	for i in range(len(lop)):
		for j in range(i+1,len(lop)):
			if len(lop[i][1])>len(lop[j][1]):
				swap = ".".join(lop[i])
				lop[i] = lop[j]
				lop[j] = swap
	return lop
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))


#prob15
def revorder(inputt):
	bnewlist = []
	inputt = inputt.split('\n')
	for i in inputt:
		bnewlist.append(inputt.pop())
	return bnewlist

p = revorder("""hey cool its is a newline.\n next next next""")
print(p)

#prob17
inp = """She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore she

