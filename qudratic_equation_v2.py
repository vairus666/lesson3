
import cmath

a = complex(input('Enter a\n'))
b = complex(input('Enter b\n'))
c = complex(input('Enter c\n'))
if a and b and c:
    d = b**2-4*a*c
    if d:
        x1 = (-b+cmath.sqrt(d))/(2*a)
        x2 = (-b-cmath.sqrt(d))/(2*a)
        print ('x1 =',x1)
        print ('x2 =',x2)
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
        print ('x1 =',x1)
        print ('x2 =',x2)

else:
    print ('Error')
