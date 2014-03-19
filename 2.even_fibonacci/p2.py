lst = [0, 1]
count = 1
while True:
	current = lst[count]
	previous = lst[count - 1]
	next = current + previous
	if next <= 4000000:
		lst.append(next)
		count += 1
	else:
		break

answer = sum([i for i in lst if i % 2 == 0])
