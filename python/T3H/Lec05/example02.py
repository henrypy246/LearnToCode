def total(a,b=3,c=2):
	return a+b-c
#print(total(a=1,c=5,b=3))

def giaiThua(n):
	if n == 0 or n ==1: return 1
	else: return n*giaiThua(n-1)
def giaiThua_(n):
	if n ==0: return 1
	else:
		mul = 1
		for x in range(2,n+1):
			mul*=x
	return mul
# print(giaiThua_(5))
# print(giaiThua(5))

def product(*nums, scale=1):
	p=scale
	for x in nums:
		p*=x
	return p
print(product(1,2,3,4))

def authorize(quote, **arg):
	print (">",quote)
	print("-"*int((len(quote)/2)))
	for k,v in arg.items():
		print(k,v,sep=': ')
authorize("If music be the food of love, play on.", 
	author="Shekespeare",act=1,scence=1,speaker='henry')
print('{0}{b}{1}{a}{2}{c}'.format(5,8,9,b=1,c='x',a='j'))