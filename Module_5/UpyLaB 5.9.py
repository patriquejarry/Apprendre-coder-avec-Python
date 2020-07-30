def anagrammes(v, w):
    if len(v) == len(w):
        for i in v:
            w = w.replace(i, '', 1)
        return len(w) == 0
    return False


print(anagrammes('marion', 'romina')) # True
print(anagrammes('bonjour', 'jour'))  # False
print(anagrammes('pate', 'patte'))    # False
