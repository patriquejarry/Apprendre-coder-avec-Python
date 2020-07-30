import math

x = float(input())
x0, x1 = 0, x
exp, sign = 3, -1

while abs(x1 - x0) > 10 ** -6:
    x0 = x1
    x1 += sign * x ** exp/math.factorial(exp)
    sign *= -1
    exp += 2
print(x1)
print("sinus", x, "=", x1, "suite ordre #", exp)