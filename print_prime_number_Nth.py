# print the prime number given  range
def CountPrimeNumber(n):          
    i = 2
    while i<=n:
        
        for j in  range(2,int(i**0.5)+1):
            if i%j==0:
                if i != j:
                    break
        else: 
            print(i,end = ' ')
        i+=1
n = int(input("Enter the number here :"))
CountPrimeNumber(n)
