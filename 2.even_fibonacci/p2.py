def main():
	fib(0, 1, 0)

def fib(x, y, z):
	add = x + y
	if add % 2 == 0:
		z += add
	print add
	if add <= 4000000:
		fib(y, add, z)
	else:
		answer = z