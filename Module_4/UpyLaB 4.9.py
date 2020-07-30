import math


def catalan(n):
    return math.factorial(2*n) // (math.factorial(n+1) * math.factorial(n))


print(catalan(4))  # 14
print(catalan(5))  # 42
print(catalan(0))  # 1
