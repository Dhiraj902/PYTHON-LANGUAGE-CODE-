# Find the factorial of list element 

def fact(arr):
    f = 1
    for i in range(1,arr+1):
        f*=i
    return f
arr = [2,4,5,6,7,3]
X = []
for i in range(len(arr)):
    S= fact(arr[i])
    X.append(S)
print(X)
