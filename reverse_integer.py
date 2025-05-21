#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


def reverse(x):
        n = False
        if x < 0:
            x = abs(x)
            n = True
        
        rev = 0
        while x > 0:
            d = x % 10
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and d > 7):
                return 0
            rev = rev * 10 + d
            x = x // 10
        
        if n:
            rev = -rev
            if rev < -2**31:
                return 0
        
        return rev
num= 123
print(reverse(num))
