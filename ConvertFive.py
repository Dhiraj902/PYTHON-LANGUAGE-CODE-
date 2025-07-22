# Convert the element Zero to five 



def convertFive(n):
        a = str(n)
        rev = ''
        for i in a:
            i = int(i)
            if i == 0:
                i+=5
                
            i = str(i)
            rev+=i
        return int(rev)
a = 1200
print(convertFive(a))
