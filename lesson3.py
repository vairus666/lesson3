# x = 10
# y = 3
# z = 14
# print(x, y, z)

"""
Математические операции
"""
# print()
# print("x + y =", x + y)
# print("x - y =", x - y)
# print("x * y =", x * y)
# print("x / y =", x / y)
# print("x // y =", x // y)
# print("x % y =", x % y)
# print("-x =", -x)
# print("abs(x) =", abs(x))
# print("divmod(x, y) =", divmod(x, y))
# print("x ** y =", x ** y)
# print("pow(x, y) =", pow(x, y))
# print(1000 / 14)
# print(1000 - 14 * 71)
# print("pow(x, y, z) =", pow(x, y, z))

"""
Битовые операции
"""
# print()
# print("x | y =", x | y)
# print("x ^ y =", x ^ y)
# print("x & y =", x & y)
# print("x << y =", x << y)
# print("x >> y =", x >> y)
# print("~x =", ~x)

"""
Системы счисления
"""
# print()
# print("Десятичная: x =", x)
# print("Двоичная: bin(x) =", bin(x))
# print("Двоичная: bin(y) =", bin(y))
# print("Восьмеричная: oct(x) =", oct(x))
# print("Шастнадцатеричная: hex(x) =", hex(x))
# print("Конвертирование из произвольной в десятичную: x =", int(str(x), y))

"""
Вещественные числа
"""
# print()
# fl_x = 0.1
# fl_xx = 0.1
# print(fl_x == fl_xx)

# print(fl_x * 10)
# fl_x1 = fl_x * 10

# print(fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x)
# fl_x2 = fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x + fl_x

# print(fl_x1 == fl_x2)
# int_a = 3 ** 1000
# print(int_a)
# a = int_a - 0.1  # OverflowError: int too large to convert to float
# print(int_a - 0.1)  # OverflowError: int too large to convert to float

# import math

# print(math.pi)
# print(math.sqrt(x * y))

# import random

# print(random.random())  # случайное число от 0 до 1.
# print(random.randrange(0, 100, 1))  # случайно выбранное число из последовательности.
# print(random.randint(0, 100))  # случайное целое число N, A ≤ N ≤ B.

"""
Комплексные числа
"""
# print()
# x_complex = complex(1, 2)
# y_complex = complex(3, 4)
# print("x =", x_complex)
# print("abs(x) =", abs(y_complex))
# print("Сопряженное число:", x_complex.conjugate())
# print("Мнимая часть:", x_complex.imag)
# print("Действительная часть:", x_complex.real)
# print("y =", y_complex)
# print("pow(y, 2) =", pow(y_complex, 2))
# print("x + y =", x_complex + y_complex)
# print("x - y =", x_complex - y_complex)
# print("x * y =", x_complex * y_complex)
# print("x / y =", x_complex / y_complex)
# print("x ** y =", x_complex ** y_complex)
# print(x_complex > y_complex)  # TypeError: '>' not supported between instances of 'complex' and 'complex'
# print("x == y", x_complex == y_complex)

"""
Строки.
"""
print()
s = "Hello World! "
# print(s)
# s[0] = "M"  # TypeError: 'str' object does not support item assignment
# s = s + "!!!"
# print("s =", s)
# S = r"c:\new.txt"
# print("S =", S)
# S = r'c:\new.txt\'  # SyntaxError: EOL while scanning string literal
# print("Hello\nWorld\n!!!")
# print("""
# "Hello"
# "World"
# '!!!'
#  """)

hello = "hello"
hello2 = "hell"
world = "World"
# print("Hello + World =", hello + " " + world)
# print("s * 3 =", s * 3)
# print("len(s) =", len(s))
# print("s[0] =", s[0])
# print("s[6] =", s[6])
# print("hello[1:5] =", hello[1:5])
# print("hello[1:5:2] =", hello[1:5:2])
# print("world[1:4:2] =", world[1:4:2])
# print("hello[-1] =", hello[-1])
# print("hello[-1:] =", hello[-1:])
# print("hello[:-1] =", hello[:-1])
# print("hello[::-1] =", hello[::-1])
# print("hello > world:", hello > world)
# print("hello < world:", hello < world)
# print("hello != world:", hello != world)
# print("hello == world:", hello == world)
# print("hello > hello2:", hello > hello2)


"""
Форматирование
"""
print()
# print("%s %s!" % (hello, world))
# print("{} {}!".format(hello, world))
# print("{0} {1}!".format(hello, world))
# print("{1} {0}!".format(hello, world))
print(f"{hello} {world}!")
