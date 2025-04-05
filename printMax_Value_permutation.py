
# print Max Value Permutation

def maxValue( arr): 
    arr.sort()
    A = 0
    mod = 1000000007  
    for i in range(len(arr)):
        A += arr[i]*i
    return A % mod
arr = [21,32,6,596,7745,365]
print(maxValue(arr))
