print('Question 1')
texte = 'bonjour'
print(texte[1:4][1])

print('Question 2')
texte = 'bonjour'
ma_liste = [texte, texte]
print(ma_liste)

print('Question 3')
texte = 'bonjour'
t1 = [texte, texte]
t1[1] = "Hello"
print(t1)

print('Question 4')
texte = 'bonjour'
t1 = [texte, texte]
t2 = t1[:]
t1[1] = "Hello"
print(t2)

print('Question 5')
def foo(liste):
    return liste + liste

x = [2,3]
x = foo(x)
print(x)


print('Question 6')
def foo(liste):
    return [liste, liste]

x = [2,3]
x = foo(x)
print(x)