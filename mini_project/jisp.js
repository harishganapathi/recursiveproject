//var n = "(begin (define r 10) (* pi (* r r)))"
var program = '(+ 1 2)'
function replaceParanthesis(program){
    	var spaceParse = []
    	var spaceRemoved = []
    	var k = ""
    	for(i in program){
      	if (program[i] == '('){
      	   k += ' ( '
      	}
      	else if (program[i] == ')'){
      	   k += ' ) '
      	}
      	else{
      	   k += "" + program[i] + ""
      	}}
    	var parsed = k.split(' ')
    	for(i in parsed){
        	if (parsed[i] != ''){
        	   spaceRemoved.push(parsed[i])
        	}
      }
    	return spaceRemoved
  }
function parse(program){
	return readFromTokens(replaceParanthesis(program))
}
/*
pp = parse(program)
console.log('pp')
console.log(pp)
console.log('pps')
*/
//readprogram = readFromTokens(replaced_string)

function readFromTokens(tokens){
  	if(tokens.length == 0){
  		throw "unexpected errr"
  	}

  	token = tokens.shift()

  	if( '(' == token){
  	L = []
  	while (tokens[0] != ')'){


  	L.push(readFromTokens(tokens))
  }
  	tokens.shift()
  	return L
  	}
  	else if (')' == token){
  	try {
  	  if (token == ')'){ throw e}
  	} catch (e) {
  	  console.log('error');
  	}
  	}
  	else{
  	return atom(token)
  	}
}
function atom(token){
if (isNaN(token) == false){
  return parseInt(token)
}
else if(isNaN(token) == true){
  return token.toString()
}
}
var env = {}
function standardEnvironment(){
//arithmetic functions
    var op ={
    add:function(a,b){
       console.log('addition')
    	return a+b
    } ,
    sub : function(a,b) {
    	console.log('subtract')
    	return a-b
    },
    mul : function(a,b) {
      console.log('multiply')
    	return a*b
    },
    div : function(a,b) {
      console.log('divide')
    	return a/b
    }
    }
    env = {
    '+' : op.add,
    '-' : op.sub,
    '*' : op.mul,
    '/' : op.div
}
return env
}
global_env = standardEnvironment()
args = []
function eval(x,env=global_env){
    if( typeof(x) == 'string' ){
        return env[x]
    }
    else if(!Array.isArray(x)){
        return x
    }
    else{
        proc = eval(x[0] , env)
        for(var arg = 1 ; arg<x.length ; arg++){
        n = eval(x[arg] , env)
        args.push(n)
    }
    return proc(args[0],args[1])
    }
}

console.log(eval(parse(program)))
