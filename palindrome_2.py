# check the number is Palindrome
def palidrom(num):
    A = num
    if num<0:
        return False
    S = int(str(num)[::-1])
    if A == S:
        return True
    return False
num = int(input("Enter the number here :"))
print(palidrom(num))
