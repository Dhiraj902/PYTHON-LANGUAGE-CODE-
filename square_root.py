"""
Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.

Floor value of any number is the greatest Integer which is less than or equal to that number.
"""
def floorSqrt( n):
    if  n == 1:
        return n
    A = 1
    B = 1
    while A <=n:
        B +=1
        A = A*A
    return B-1
n = 2
print(floorSqrt(n))
