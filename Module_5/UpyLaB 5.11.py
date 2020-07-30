def intersection(v, w):
    inter = ''
    inter_aux = ''
    for i in range(len(v)):
        for j in range(i+1):
            inter_aux = v[j:i + 1]
            if w.find(inter_aux) != -1:
                if len(inter) < len(inter_aux):
                    inter = inter_aux
            else:
                inter_aux = ''
    return inter


print(intersection('programme', 'grammaire'))  # 'gramm'
print(intersection('salut', 'merci'))          # ''
print(intersection('merci', 'adieu'))          # 'e'
print(intersection('crane', 'carne'))          # 'ne'
print(intersection('ironique', 'onirique'))    # 'ique'
