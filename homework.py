#Prime number

x = int(input('Enter number\n'))
if x % 2 == 0:
    print (' Your number is even')
d = 3
while d * d <= x and x % d != 0:
        d += 2
if d * d > x:
    print ('Your number is prime')
else:
    print ('Your number is not prime')

# NOD

a = int(input(' Enter number 1\n'))
b = int(input(' Enter number 2\n'))
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print('NOD = ', a + b)

# NOK

a = int(input(' Enter number 1\n'))
c = a
b = int(input(' Enter number 2\n'))
d = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print('NOK = ', abs(c * d) / (a + b))
