# Factorial program using the map function 

def fact(arr):
    f = 1
    for i in range(1,arr+1):
        f*=i
    return f
arr = [2,4,5,6,7,3]
S = map(fact,arr)
print(list(S))
