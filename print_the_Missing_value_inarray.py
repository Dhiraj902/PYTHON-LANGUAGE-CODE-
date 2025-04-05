# print the Missing Value in array
# Using Formula
# method 1
def missingvalue(arr):
    A = len(arr)+1
    Z = A*(A+1)//2
    return Z - sum(arr)
arr = [1, 5 ,3 ,7, 6, 4]
print(missingvalue(arr))



# Without Using Formula
# method 2
def missingvalue(arr):
    arr.sort()
    A = len(arr)
    for i in range(A):
        if  arr[i] != i+1:
            return i+1
    return A+1
arr =[8, 5, 1,3 ,7,4, 2,6]
print(missingvalue(arr))

