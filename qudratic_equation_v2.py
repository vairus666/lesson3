import cmath

a = complex(input('Enter a\n'))
b = complex(input('Enter b\n'))
c = complex(input('Enter c\n'))
if a and b and c:
    """
    Введи коэфиенты уравнения формата x^2+x+c=0

    a -- коэфициент при x^2
    b -- коэфициент при x
    c -- константа
    d -- дискрименант
    """
    d = b**2 - 4*a*c
    if d:
        x1 = (-b+cmath.sqrt(d)) / (2*a)
        x2 = (-b-cmath.sqrt(d)) / (2*a)
        print(f'x1 ={x1:.3f}')
        print(f'x2 ={x2:.3f}')
    else:
        x = (-b)/(2*a)
        print ('x = ', x)
elif a and b and c == 0:
    print ('x1 = 0')
    x2 = (-b)/a
    print ('x2 = ',x2)
elif a and b == 0 and c:
        x1 = cmath.sqrt(-c/a)
        x2 = -cmath.sqrt(-c/a)
        print(f'x1 ={x1:.3f}')
        print(f'x2 ={x2:.3f}')
else:
    print ('Error')

