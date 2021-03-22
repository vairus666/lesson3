comand = input('what are we checking?(NOD, NOK, prime)\n')
while comand.lower() != 'exit':
    # Является число простым или нет.
    if comand.lower() == 'prime':
        x = int(input('Enter number\n'))
        if x%2 == 0:
            print (' Your number is even')
        d = 3
        while d*d <= x and x%d != 0:
                d += 2
        if d*d > x:
            print ('Your number is prime')
            comand = input('what are we checking?(NOD, NOK, prime)\n')
        else:
            print ('Your number is not prime')
            comand = input('what are we checking?(NOD, NOK, prime)\n')

    # Считает НОД
    elif comand.lower() == 'NOD':
        a = int(input('Enter number 1\n'))
        b = int(input('Enter number 2\n'))
        while a != 0 and b != 0:
            if a > b:
                a = a%b
            else:
                b = b%a
        print('NOD = ', a+b)
        comand = input('what are we checking?(NOD, NOK, prime)\n')

    # Считает НОК
    elif comand.lower() == 'NOK':
        a = int(input('Enter number 1\n'))
        c = a
        b = int(input('Enter number 2\n'))
        d = b
        while a != 0 and b != 0:
            if a > b:
                a = a%b
            else:
                b = b%a
        print('NOK = ', abs(c*d) / (a+b))
        comand = input('What are we checking?(NOD, NOK, prime)\n')
    else:
        print('Unknown comand')
        comand = input('What are we checking?(NOD, NOK, prime)\n')
