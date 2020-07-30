def my_pow(m, b):
    if type(m) != int or type(b) != float:
        return None
    return [b ** x for x in range(m)]


print(my_pow(3, 5.0))       # [1.0, 5.0, 25.0]
print(my_pow(3.0, 5.0))     # None
print(my_pow('a', 'b'))     # None
