#spiral matrix

m, n = list(map(int, input().split()))
matrix = [["0".ljust(3) for j in range(n)] for i in range(m)]
directions = ["right", "down", "left", "up"]
matrix_area = n * m
biase = 0
count = 0
nums = range(1, matrix_area + 1)
stop_flag = False

for i in range(m + n):
	if stop_flag: break
	direction = directions[i % 4]
	
	for j in range(biase, [n, m][i % 2]):
		if count == len(nums):
			stop_flag = True
			break
		number = str(nums[count]).ljust(3)
		if direction == "right":
			matrix[biase][j] = number
		if direction == "down":
			matrix[j][~biase + 1] = number
		if direction == "left":
			matrix[~biase + 1][~j] = number
		if direction == "up":
			matrix[~j][biase - 1] = number
		count += 1

	if (i + 1) % 4 == 0:
		n -= 1
	if (i + 1) % 4 == 2:
		m -= 1
	if direction == "right":
		biase += 1

for i in matrix: print(*i)
print()
#print(*list(map(list, zip(*matrix))))