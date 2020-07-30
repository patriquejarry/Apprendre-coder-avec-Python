print("Question 1 ----------------------")
def foo_1(x) :
    print(2*x)
a = 4
foo_1(2*a)

print("Question 2 ----------------------")
def foo_2(x) :
    x = 2*x
a = 4
foo_2(2*a)
print(a)

print("Question 3 ----------------------")
def foo_3(x):
    x = 2*x
x = 4
foo_3(2*x)
print(x)

print("Question 4 ----------------------")
def foo_4(x, y) :
    x, y = y, x
a = 4
b = 8
foo_4(a, b)
print(a, b)

print("Question 5 ----------------------")
def foo_5(x, y) :
    return  y, x
a = 4
b = 8
a, b = foo_5(a, b)
print(a, b)

print("Question 6 ----------------------")
def foo_6(x, y) :
    return  y, x
a = 4
b = 8
foo_6(a, b)
print(a, b)