
print('Question 1')
s = [1,2,3,4,5,6,7]
s.append(0)
print(s)

print('Question 2')
s = [1,2,3,4,5,6,7]
s[len(s):len(s)] = [0]
print(s)

print('Question 3')
s = [1,2,3,4,5,6,7]
s.extend([0])
print(s)

print('Question 4')
s = [1,2,3,4,5,6,7]
s.insert(len(s),0)
print(s)

print('Question 5')
s = [1,2,3,4,5,6,7]
s[0:1] = []
print(s)

print('Question 6')
s = [1,2,3,4,5,6,7]
del s[0]
print(s)

print('Question 7')
s = [1,2,3,4,5,6,7]
del s[-len(s)]
print(s)

print('Question 8')
s = [1,2,3,4,5,6,7]
del s[len(s)-1]
print(s)

print('Question 9')
s = [1,2,3,4,5,6,7]
s[len(s)-1:] = []
print(s)
