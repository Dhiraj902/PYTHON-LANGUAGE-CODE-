# Check the number is power of two 

def poweroftwo(n):
    if n<=0:
        return False
    return (n & (n-1))==0
n = int(input("Enter the number:"))
print(poweroftwo(n))
