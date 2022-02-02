a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1):
    j = c
    if i == a:
        while True:
            if j > d:
                print('\n')
                break
            print('\t', end = ' ')
            print(j, end = ' ')
            j += 1
    for j in range(c, d + 1):
        if j == c:
            print('', i, end = '\t')
        print('|', i * j, end = ' |\t')
    print('\n')