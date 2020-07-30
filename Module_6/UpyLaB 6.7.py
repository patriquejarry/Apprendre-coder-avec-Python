def even(max_nb):
    """fonction qui renvoie l’ensemble des nombres naturels pairs inférieurs ou égaux à max_nb"""
    return {x for x in range(max_nb+1) if x % 2 == 0}


def prime_numbers(max_nb):
    """la fonction qui renvoie l’ensemble des nombres premiers inférieurs ou égaux à max_nb."""

    primes = set()
    i = 2
    while i <= max_nb:
        res = True
        for n in range(2, i):
            if i % n == 0:
                res = False
        if res:
            primes.add(i)
        i += 1

    return primes


def prime_odd_numbers(numbers):
    """la fonction qui reçoit une liste de nombres et qui renvoie un couple d’ensembles contenant respectivement
    les nombres premiers présents dans la liste et les nombres impairs."""

    max = sorted(numbers, reverse=True)[0]
    pairs = even(max)
    premiers = prime_numbers(max)

    return set([x for x in numbers if x in premiers]), set([x for x in numbers if x not in pairs])


#print(even(10))
#print(prime_numbers(10))

print(prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18]))
# ({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17})

print(prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18]))
# (set(), {1, 9, 15, 21})



print(even(46)) # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46}
print(even(95)) # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94}
print(even(75)) # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74}

print(prime_numbers(34)) # {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
print(prime_numbers(21)) # {2, 3, 5, 7, 11, 13, 17, 19}
print(prime_numbers(99)) # {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
print(prime_numbers(92)) # {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89}

print(prime_odd_numbers([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97])) # ({97, 37, 5, 41, 73, 13, 17, 61, 53, 89, 29}, {1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97})
print(prime_odd_numbers([100, 93, 86, 79, 72, 65, 58, 51, 44, 37, 30, 23, 16, 9, 2])) # ({2, 23, 37, 79}, {65, 37, 9, 79, 51, 23, 93})
print(prime_odd_numbers([0, 21, 42, 63, 84])) # (set(), {21, 63})
print(prime_odd_numbers([401, 568, 735, 902, 1069, 1236])) # ({401, 1069}, {401, 1069, 735})
