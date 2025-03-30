# print the 1 - N netural Number using Recursion 
def num(n):
    if n==0:
        return n
    
    else:
        num(n-1)
        print(n,end=' ') 
(num(12))
