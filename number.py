#Выводит частоту вхождения цифр в диапазоне
x = int(input("Enter start of range\n"))
y = int(input("Enter end of range\n"))
num0 = num1 = num2 = num3 = num4 = num5 =\
num6 = num7 = num8 = num9 = k = 0
l = list(range(x, y))
m = "".join(map(str, l))
o = len(m)
while k < o:
    if m[k] == "0":
        k += 1
        num0 += 1
    elif m[k] == "1":
        k += 1
        num1 += 1
    elif m[k] == "2":
        k += 1
        num2 += 1
    elif m[k] == "3":
        k += 1
        num3 += 1
    elif m[k] == "4":
        k += 1
        num4 += 1
    elif m[k] == "5":
        k += 1
        num5 += 1
    elif m[k] == "6":
        k += 1
        num6 += 1
    elif m[k] == "7":
        k += 1
        num7 += 1
    elif m[k] == "8":
        k += 1
        num8 += 1
    else:
        k += 1
        num9 += 1


print(f'0 = {num0}, 1 = {num1}, 2 = {num2}, 3 = {num3}, 4 = {num4},\
        5 = {num5} 6 = {num6}, 7 = {num7}, 8 = {num8}, 9 = {num9}') 
