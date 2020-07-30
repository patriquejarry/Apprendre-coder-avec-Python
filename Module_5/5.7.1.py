
print('Question 1')
x = list(enumerate('bonjour'))
print(x)

print('Question 2')
x = list(zip(range(10), 'bonjour'))
print(x)

print('Question 3')
x  = [couple for couple in enumerate('bonjour')]
print(x)

print('Question 4')
x = 'bonjour'
x = [(i, x[i]) for i in range(len(x))]
print(x)

print('Question 5')
x = []
#for i in range(len('bonjour')):
#    x.append((i, x[i]))
# SE ARRETE A CAUSE D'ERREUR
print(x)

print('Question 6')
x = []
for couple in enumerate('bonjour'):
    x.append(couple)
print(x)

print('Question 7')
x = []
for i, c in enumerate('bonjour'):
    x.append((i, c))
print(x)

print('Question 8')
voyelles = "aeiouy"
x = list(enumerate('bonjour'))
for i in range(len(x)-1,-1,-1):
    if x[i][1] in voyelles:
       del x[i]
print(x)

print('Question 9')
voyelles = "aeiouy"
x = [couple for couple in enumerate('bonjour') if couple[1] not in voyelles]
print(x)

print('Question 10')
voyelles = "aeiouy"
t = 'bonjour'
x = [(i, t[i]) for i in range(len(t)) if t[i] not in voyelles]
print(x)

print('Question 11')
x = []
voyelles = "aeiouy"
t = 'bonjour'
for i in range(len('bonjour')):
    if t[i] not in voyelles:
        x.append((i, t[i]))
print(x)

print('Question 12')
voyelles = "aeiouy"
x = []
for i, c in enumerate('bonjour'):
    if c not in voyelles:
        x.append((i, c))
print(x)

print('Question 13')
voyelles = "aeiouy"
x = list(enumerate('bonjour'))
#for i in range(len(x)):
#    if x[i][1] in voyelles:
#        del x[i]
# SE ARRETE A CAUSE D'ERREUR
print(x)

print('Question 14')
voyelles = "aeiouy"
x = list(enumerate('bonjour'))
i = 0
#while i < len(x):
#    if x[i][1] in voyelles:
#        del x[i]
#        i = i + 1
# NE SE ARRETE PAS - RESTE EN BOUCLE
print(x)

print('Question 15')
voyelles = "aeiouy"
x = list(enumerate('bonjour'))
i = 0
while i < len(x):
    if x[i][1] in voyelles:
        del x[i]
    else:
        i = i + 1
print(x)
