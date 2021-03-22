"""
Задача FizzBuzz

При нахождения числа, делящегося нацело на 3 выводдить Fizz.
При нахождения числа, делящегося нацело на 5 выводдить Buzz.
При нахождения числа, делящегося нацело на 3 и на 5 выводдить FizzBuzz.
"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
