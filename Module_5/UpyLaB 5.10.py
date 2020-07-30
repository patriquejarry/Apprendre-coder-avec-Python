def dupliques(v):
    for i in v:
        if v.count(i) != 1:
            return True
    return False


print(dupliques([1, 2, 3, 4]))          # False
print(dupliques(['a', 'b', 'c', 'a']))  # True
print(dupliques('abcda'))               # True
