print("Question 1 --------------")
r = {'cacao'}
s = set('cacao')
t = {'a', 'e', 'i', 'o', 'u', 'y'}
print(len(r))

print("Question 2 --------------")
r = {'cacao'}
s = set('cacao')
t = {'a', 'e', 'i', 'o', 'u', 'y'}
print(len(s))

print("Question 3 --------------")
r = {'cacao'}
s = set('cacao')
t = {'a', 'e', 'i', 'o', 'u', 'y'}
print(s & t)

print("Question 4 --------------")
r = {'cacao'}
s = set('cacao')
t = {'a', 'e', 'i', 'o', 'u', 'y'}
#s |= {'x'}
s.add('x')
print(s)

print("Question 5 --------------")
r = {'cacao'}
s = set('cacao')
t = {'a', 'e', 'i', 'o', 'u', 'y'}
#s -= {'b'}
s.discard('b')
#s.remove('b')
print(s)

print("Question 6 --------------")
d = {}
b = 4.5

d[1] = 22
d[3.14] = 24
d[b] = 90
d['b'] = 25
#d[(1,2)]'X'
#d[[3,4]] = 32
d[2] = (3,4)
d[5,4] = [5,4]