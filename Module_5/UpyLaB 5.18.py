def my_filter(lst, f):
    return [i for i in lst if f(i)]
    #   m = []
    #   for i in lst:
    #       if f(i):
    #           m.append(i)
    #   return m


print(my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int)))   # [666, 42]
print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0))                                # [-2, -5, -6]

