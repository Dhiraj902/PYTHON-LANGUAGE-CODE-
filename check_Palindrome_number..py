# Check The Given Number is Palindrome or not 

    
def palidrom(num):
    A = num
    if num<0: # if The Number is nigeive then return False 
        return False 
    S = int(str(num)[::-1])
    if A == S:
        return True
    return False
num = 0
print(palidrom(num))
