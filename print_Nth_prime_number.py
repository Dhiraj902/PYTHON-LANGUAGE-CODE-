# print the nth prime number


def NthPrime(n):
    c = 0
    i = 2
    while True:
        
        for j in  range(2,i+1):
            if i%j==0:
                if i != j:
                    break
                if i==j:
                    c+=1
                    print(i,end = ' ')
        i+=1
        if c == n:
            break          
n = int(input("Enter the number here: "))
NthPrime(n)
