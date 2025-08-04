"""
Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.
"""


def count_digit(n):
    count = 0
    A = n
    while n>0:
        B = n%10
        if B!= 0 and A%B == 0:
            count +=1
        n = n//10
    return count
n = 23
print(count_digit(n))
