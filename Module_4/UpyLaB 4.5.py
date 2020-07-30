import random

DICE_MIN = 1
DICE_MAX = 6


def alea_dice(s):
    random.seed(s)
    a = random.randint(DICE_MIN, DICE_MAX)
    b = random.randint(DICE_MIN, DICE_MAX)
    c = random.randint(DICE_MIN, DICE_MAX)

    res = a != b and a != c and b != c
    if res:
        for num in (a, b, c):
            if res and num != 4 and num != 2 and num != 1:
                res = False
    return res


print(alea_dice(1))   # False
print(alea_dice(25))  # True
