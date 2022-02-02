#is magic square?

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
numbers = [a for b in matrix for a in b]
if 0 in numbers: is_magic = False

diagonal_sum = sum([matrix[i][i] for i in range(n)])
oth_diagonal_sum = sum([matrix[i][~i] for i in range(n)])
is_magic = True

for i in range(n):
	if not is_magic: break
	if (i + 1) not in numbers: is_magic = False
	col_sum = sum([matrix[k][i] for k in range(n)])
	row_sum = sum(matrix[i])
	if not col_sum == row_sum == diagonal_sum == oth_diagonal_sum:
		is_magic = False

print("YES" if is_magic else "NO")