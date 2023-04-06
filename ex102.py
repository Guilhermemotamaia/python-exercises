import math
def s():
    a = int(input('what fatorial your want know?'))
    c = a
    while c > 0:
        print(c, end='')
        if c != 1:
            print(' x', end=' ')
        else:
            print(f'= {math.factorial(a)}')
        c -= 1
s()
def fac(a):
    s = math.factorial(a)
    print(s)
fac(5)
fac(2)
fac(6)






