# Rotate Array using Slicing


def rotate_array(arr):
    n = len(arr)
    arr[:] = arr[n-1:] + arr[0:n-1]
    return arr
arr = [23,45,56,7,89,9]
print(rotate_array(arr))
