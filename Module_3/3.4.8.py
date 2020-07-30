print("Question 1 --------------")
x = 10
while x > 0 :
    x = x - 1
    print(x)

print("Question 2 --------------")
x = 10
while x >= 0 :
    x = x - 2
    print(x)

print("Question 3 --------------")
x = 1
while x < 10 :
    x = x + x
    print(x)

print("Question 4 --------------")
x = 1
limite = 20 # le while boucle indéfiniment mais on l'arrete
while x < 10 and limite > 0:
    x = x * x
    print(x)
    limite -= 1

print("Question 5 --------------")
x = 2
while x < 10 :
    x = x * x
    print(x)

print("Question 6 --------------")
for x in range(5):
    for y in range(4):
        print(x, y)
