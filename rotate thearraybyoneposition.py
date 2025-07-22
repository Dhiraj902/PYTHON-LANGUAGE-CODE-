#Given an array arr, rotate the array by one position in clockwise direction.
def rotateArray(arr):
    temp = A[-1]
    for i in range(len(A)-1,-1,-1):
        A[i] =  A[i-1]
    A[0] = temp
    return A
