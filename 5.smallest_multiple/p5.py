count = 20
while True:
	print "{:,d}".format(count)
	token = True
	for i in range(2, 20):
		if count % i != 0:
			token = False
	if token:
		break
	else:
		count += 20

answer = count