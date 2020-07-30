l = input()
a = float(input())

if "T" == l :
    print(2 ** 0.5 * a ** 3 / 12)
elif "C" == l :
    print(a ** 3)
elif "O" == l :
    print(2 ** 0.5 * a ** 3 / 3)
elif "D" == l :
    print((15 + 7 * 5 ** 0.5) * a ** 3 / 4)
elif "I" == l :
    print(5 * (3 + 5 ** 0.5) * a ** 3 / 12)
else:
    print("Polyèdre non connu")

# t = 2 ** 0.5 * a ** 3 / 12
# c = a ** 3
# o = 2 ** 0.5 * a ** 3 / 3
# d = (15 + 7 * 5 ** 0.5) * a ** 3 / 4
# i = 5 * (3 + 5 ** 0.5) * a ** 3 / 12

# print(t)
# print(c)
# print(o)
# print(d)
# print(i)
