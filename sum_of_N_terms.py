# print the sum of n-terms
# 1**3 + 2**3 + 3**3 +4**3 +5**3 = 225
def sumofN_terms(n):
    A = (n*(n+1)//2)**2
    return A
n = 5 # n = 1+2+......+n-1
print(sumofN_terms(n))
