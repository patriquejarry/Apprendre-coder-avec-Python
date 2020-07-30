def next_line(line):
    """ fonction qui reçoit une liste d’entiers décrivant une ligne de cette suite,
    et qui retourne la liste correspondant à la ligne suivante. """

    if len(line) == 0:
        return [1]

    result = []
    n_aux = ""
    count = 0
    for n in line:
        if n != n_aux and n_aux != "":
            result.append(count)
            result.append(n_aux)
            count = 0
        count += 1
        n_aux = n
    result.append(count)
    result.append(n_aux)

    return result


print(next_line([1, 2, 1, 1]))  # [1, 1, 1, 2, 2, 1]
print(next_line([1]))           # [1, 1]
print(next_line([]))            # [1]

print(next_line([]))                              # [1]
print(next_line([1]))                             # [1, 1]
print(next_line([1, 1]))                          # [2, 1]
print(next_line([2, 1]))                          # [1, 2, 1, 1]
print(next_line([1, 2, 1, 1]))                    # [1, 1, 1, 2, 2, 1]
print(next_line([1, 1, 1, 2, 2, 1]))              # [3, 1, 2, 2, 1, 1]
print(next_line([3, 1, 2, 2, 1, 1]))              # [1, 3, 1, 1, 2, 2, 2, 1]
print(next_line([1, 3, 1, 1, 2, 2, 2, 1]))        # [1, 1, 1, 3, 2, 1, 3, 2, 1, 1]
print(next_line([1, 1, 1, 3, 2, 1, 3, 2, 1, 1]))  # [3, 1, 1, 3, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1]
print(next_line([3, 1, 1, 3, 1, 1, 2, 2, 3, 3, 2, 3, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 3, 2, 1, 1]))
# [1, 3, 2, 1, 1, 3, 2, 1, 2, 2, 2, 3, 1, 2, 1, 3, 1, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2, 1, 1, 3, 1, 2, 2, 1]
