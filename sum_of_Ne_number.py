# sum of N netural number using Formula

def sum_n(n):
    sum = (n*(n+1))//2
    return sum
n = int(input("Enter the  netural number: "))
print(f"The sum of {n} natural number is = ",sum_n(n))
