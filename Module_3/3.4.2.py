x = int(input("x = "))
y = int(input("y = "))
while y > 0:
    x, y = y, x % y
    print(x, y)
print("pgcd = ", x)