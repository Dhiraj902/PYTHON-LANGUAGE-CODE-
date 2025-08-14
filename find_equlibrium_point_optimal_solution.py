# Find The Equlibrium Point in The Array 
# Optimal Solution 
def equlibrium_point(arr):
    n = len(arr)
    if n == 1:
        return -1
    total_sum = sum(arr)
    left_sum = 0
    for i in range(n):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]
    return -1


arr = [1,1,1,1]
print(equlibrium_point(arr))




#2 
def equlibrium_point(arr):
    n = len(arr)
    
    if n == 1:
        return -1
    left_sum  = 0
    right_sum = 0
    for i in range(1,n):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        if left_sum == right_sum:
            return i
        
    return -1
arr = [1,1,1,1]
print(equlibrium_point(arr))
