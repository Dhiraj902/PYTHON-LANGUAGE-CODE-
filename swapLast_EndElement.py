# Swap the array element from  kth vlaue from starting and ending both

def swapLast_EndElement(arr,k):
    
    if k <= len(arr):
        fir = arr[k-1]
        las = arr[-k]
    
        arr[k-1] = las
        arr[-k] = fir
    
    return arr
arr = [1, 2, 33, 4, 5, 6, 7, 8]
k = 3
print(swapLast_EndElement(arr,k))
