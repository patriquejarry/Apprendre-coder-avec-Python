v = 0
n = int(input())
if n >= 0:
    for i in range(n):
        v += int(input())
else:
    n = 0
    while n != "F":
        v += int(n)
        n = input()

print(v)
