def plus_grand_bord(mot):
    bord = ''
    for i in range(1, len(mot)-1):
        if mot[:i] == mot[len(mot)-i:]:
            if len(bord) < len(mot[:i]):
                bord = mot[:i]
    return bord


print(plus_grand_bord('abdabda'))  # 'abda'
print(plus_grand_bord('abcabd'))   # ''
print(plus_grand_bord('abcba'))    # 'a'
