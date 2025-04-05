# Armstrong Numbers
#  are given a 3-digit number n, Find whether it is an Armstrong number or not.

def ArmstrongsNumber(num):
    A = 0
    X = num
    while(num!=0):
        S = num%10
        A += S**3
        num = num//10
    if X == A:
        print(f"The number {X} is  ArmstrongsNumber :")
    else:
        print(f"The number {X} is not ArmstrongsNumber :")
num = int(input("Enter the number  here:"))
ArmstrongsNumber(num)
