sum_square = 1

for i in range(2, 101):
	sum_square += i ** 2

square_sum = sum(range(1, 101)) ** 2

answer = square_sum - sum_square