def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    res = True
    if n < 2:
        res = False
    else:
        for i in range(2, n):
            if n % i == 0:
                res = False

    return res


def prime_numbers(nb):
    if type(nb) != int or nb < 0:
        return None

    primes = []
    i = 2
    while (len(primes) != nb):
        if(premier(i)):
            primes.append(i)
        i+=1
    return primes


print(prime_numbers(4))     # [2, 3, 5, 7]
print(prime_numbers(-2))    # None
print(prime_numbers("4"))   # None
print(prime_numbers(None))  # None
print(prime_numbers(4.0))   # None
print(prime_numbers(0))   # None
