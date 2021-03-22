#XOR шифрование
key = 25
a = input ('Do you want to encrypt?(Yes or No)\n')
if a.lower() == "yes":
    orig = input('Enter orginal message\n')
    crypt = ""
    for i in orig:
	    try:
		    crypt += chr(ord(i)^ord(key))
	    except TypeError:
		    crypt += chr(ord(i)^key)
    print('Encripted message \n', crypt)
elif a.lower() == "no":
    a = input('Do you want to decode?(Yes or No)\n')
    if a.lower() == "yes":
        orig = input('Enter orginal message\n')
        crypt = ""
        for i in orig:
            try:
                crypt += chr(ord(i)^ord(key))
            except TypeError:
                crypt += chr(ord(i)^key)
        print('Encripted message \n', crypt)
    elif a.lower == 'no':
        print ('Bye Bye')
    else:
        print ("I don't understand you. Bye")
else:
    print ("I don't understand you. Bye")
