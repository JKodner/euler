nums = []
for i in range(100, 1001):
	for x in range(100, 1001):
		product = str(i * x)
		if product[::1] == product[::-1]:
			nums.append(product)

answer = max(map(int, nums))