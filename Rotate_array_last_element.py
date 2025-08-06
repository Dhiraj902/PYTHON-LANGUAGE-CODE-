# Rotate The Array Element 




def rotate_Array(arr):
    temp = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = temp
    return arr
arr = [23,45,56,7,89,9]
print(rotate_Array(arr))
