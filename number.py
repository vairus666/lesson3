#The frequency of using digits in a range of numbers.

x = int(input ('Enter start of range\n'))
y = int(input ('Enter end of range\n'))
a = b = c = d = e = f = g = h = i = j = k = 0
l = list(range(x,y))
m = ''.join(map(str,l))
o = len(m)
while k < o:    
        if m[k] == '0':
            k +=1
            a +=1
        elif m[k] == '1':
            k +=1
            b +=1
        elif m[k] == '2':
            k +=1
            c +=1
        elif m[k] == '3':
            k +=1
            d +=1     
        elif m[k] == '4':
            k +=1
            e +=1   
        elif m[k] == '5':
            k +=1
            f +=1 
        elif m[k] == '6':
            k +=1
            g +=1
        elif m[k] == '7':
            k +=1
            h +=1
        elif m[k] == '8':
            k +=1
            i +=1
        else:
            k +=1
            j +=1
            
print ('0 = ', a, '\n1 = ', b, '\n2 = ', c,'\n3 = ', d,'\n4 = ', e,'\n5 = ', f,'\n6 = ', g,'\n7 = ', h,'\n8 = ', i,'\n9 = ', j)
