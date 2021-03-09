a = input ('Do you want to encrypt?(Yes or No)\n')
if a.lower() == "yes":
    orig = input('Enter orginal message\n')
    key = 25
    crypt = ""
    for i in orig:
	    try:
		    crypt += chr(ord(i)^ord(key))
	    except TypeError:
		    crypt += chr(ord(i)^key)
    print('Encripted message \n', crypt)
elif a.lower() == "no":
    a = input('Do you want to decode?(Yes or No)\n')
    if  a.lower() == 'yes':
        key = 25
        encr = input('Enter encrypted message\n')
        decrypt = ""
        for j in encr:
	        try:
		        decrypt += chr(ord(j)^ord(key))
	        except TypeError:
		        decrypt += chr(ord(j)^key)
        print('Encripted message \n', decrypt )

    elif a.lower == 'no':
        print ('Bye Bye')
    else:
        print ("I don't understand you. Bye")
else:
    print ("I don't understand you. Bye")
