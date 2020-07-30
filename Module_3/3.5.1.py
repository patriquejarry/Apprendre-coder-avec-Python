n = int(input())

fn1, fn = 0, 1

if n > 0:
    print(fn1)
    n -= 1

if n > 0:
    for i in range(n) :
        print(fn)
        fn, fn1 = fn1 + fn, fn
