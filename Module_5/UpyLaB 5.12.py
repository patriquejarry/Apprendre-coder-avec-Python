def my_insert(v, w):
    if type(w) == int:
        a = v.copy()
        a.append(w)
        return sorted(a)

    return None


print(my_insert([1, 3, 5], 4))    # [1, 3, 4, 5]
print(my_insert([2, 3, 5], 1))    # [1, 2, 3, 5]
print(my_insert([2, 3, 5], 0.5))  # None
print(my_insert([2, 3, 5], 6))    # [2, 3, 5, 6]
print(my_insert([], 5))           # 5
