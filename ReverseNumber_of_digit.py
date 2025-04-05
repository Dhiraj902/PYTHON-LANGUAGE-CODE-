# Reverse the given number of digit
#  given Number without Space
def reverseNumber(n):
    d=0
    while(n!=0):
        x=n%10
        d =d*10+x
        n= n//10
    print(d)
n = int(input("Enter the number here:"))
reverseNumber(n)
