# Factodial of Number using recursion 
# without using loop
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n = int(input("Enter the Number ->> "))
print(f"The factorial of {n} is : ",fact(n))


# Factorial using loop

def fact(n):
    A = 1
    if n==0:
        return 1
    for i in range(1,n+1):
        A*=i
    return A
n = int(input("Enter the number : "))
print(f"The factorial of {n} is : ",fact(n))
    
        
