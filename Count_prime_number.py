# Count the prime number of given range

def CountPrimeNumber(n):          
    result = 0
    i = 2
    while i<=n:
        
        for j in  range(2,int(i**0.5)+1):
            if i%j==0:
                if i != j:
                    break
        else: 
            result +=1
        i+=1
    return result
n = int(input("Enter the number here :"))
print(CountPrimeNumber(n))
