def gen_finbonnaci(n):
	a = 0
	b = 1	
	
	for i in range(n):
		if (i == 0):
			yield 0
		elif (i == 1):
			yield 1
		else:
			c = a + b
			a = b
			b = c
			yield c


for i in gen_finbonnaci(10):
	print(i)
