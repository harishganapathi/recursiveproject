sentence = "aaabccdeeeeeffg"
codes = {}

function wordfrequency(sentence)
{
				mydict = {}
				for(i in sentence)
				{
				var j = sentence[i]
				if (j in mydict)
				{
					mydict[j] += 1
				}
				else{
					mydict[j] = 1
				}
}
return mydict
}


frequency = wordfrequency(sentence)
console.log(frequency)



function sortfreq(frequency)
{
				key = Object.keys(frequency)
				freq_list = []
				for(i in key)
				{
					freq_list.push([mydict[key[i]],key[i]])
				}
				return freq_list
}
sortd = sortfreq(frequency)
console.log(sortd)

function buildTree(sortd)
{
			while( sortd.length >1)
			{
				least = sortd.slice(0,2)
				rest = sortd.slice(2,sortd.length)
				combine = least[0][0] + least[1][0]
				rest.push([combine,least])
				s = rest
				s.sort()
				sortd = s
			}
			return sortd[0]

}

tree = buildTree(sortd)
console.log(tree)

function trimTree(tree){
				var p = tree[1]
				if (typeof(p) == typeof(""))
				{
					return p
				}
				else
				{
					return [trimTree(p[0]),trimTree(p[1])]
				}
}

trim = trimTree(tree)
console.log(trim)

function assignCode(node , pat = "")
{
				if(typeof(node) == typeof(""))
				{
					codes[node] = pat
				}
				else{
				assignCode(node[0] , pat+"0")
				assignCode(node[1],pat+"1")
}
}

fin = assignCode(trim , "")
console.log(codes)


function encode(sentence)
{
				output = ""
				for(j in sentence){
				output += codes[sentence[j]]
				}
				return output
}
op = encode(sentence)
console.log(op)
