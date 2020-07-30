def my_insert(v, w):
    assert type(w) == int
    v.append(w)
    v.sort()


l = [1, 3, 5]
my_insert(l, 4)    # [1, 3, 4, 5]
print(l)

l = [1, 3, 5]
my_insert(l, 'a')   # AssertionError
print(l)
