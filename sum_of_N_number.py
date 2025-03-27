# Sum of netural number 

def sum_n(n):
    sum = 0
    if n<=0:
        return 0
    else:
        for i in range(1,n+1):
            sum += i
        return sum
n = int(input("Enter the netural number :"))
print(f"The sum of {n} natural number  is = ",sum_n(n))
