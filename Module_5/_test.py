prem = sec = [1, 3]
print(prem, '-', sec)

prem[0] = 2
print(prem, '-', sec)

prem.append(5)
print(prem, '-', sec)

prem.extend([7, 11])
print(prem, '-', sec)

prem.append([7, 11])
print(prem, '-', sec)
