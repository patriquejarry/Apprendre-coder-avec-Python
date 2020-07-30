x = int(input())
for i in range(1, x + 1):
    print(' ' * (x-i), sep = '', end = '')
    for j in range(i, i*2):
        print(j % 10, sep = '', end = '')
    for j in range(j-1, i-1, -1):
        print(j % 10, sep = '', end = '')
    print()