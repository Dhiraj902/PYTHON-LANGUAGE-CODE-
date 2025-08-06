# Kth roataion Element using Slicing


def kth_rotate(arr,k):
    n = len(arr)
    k = k%n
    arr[:] = arr[n-k:] + arr[:n-k]
    return arr
arr = [23,45,56,7,89,9]
k = 11
print(kth_rotate(arr,k))
