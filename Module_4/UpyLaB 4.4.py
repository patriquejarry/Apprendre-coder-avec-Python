def fibo(n):
    x2 = 0
    x1 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        for i in range(1, n):
            x2, x1 = x1, x1 + x2
        return x1


n = int(input())
for i in range(n):
    print(fibo(i))