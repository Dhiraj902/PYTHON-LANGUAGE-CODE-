# print the N -1 netural Number using Recursion 
def num(n):
    if n==0:
        return n
    
    else:
        print(n,end=' ')
        num(n-1)
(num(12))
