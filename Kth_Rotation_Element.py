# Rotate The kth Rotation   Array Element 


def kth_rotate(arr,k):
    n = len(arr)
    A = k%n
    for _ in range(A):
        R = arr.pop()
        arr.insert(0,R)
    return arr
arr = [23,45,56,7,89,9]
k = 11
print(kth_rotate(arr,k))
