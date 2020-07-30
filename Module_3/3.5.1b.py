t = int(input())

fn1, fn = 0, 1

if t > fn1:
    print(fn1)

while t > fn:
    print(fn)
    fn1, fn = fn, fn + fn1
