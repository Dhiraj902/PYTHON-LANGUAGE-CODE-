 # Find the max Element of Array 

# 1.
arr = [5,6,1,7,2,9,4]
A  = max(arr)
print(A)


# 2.
def max_element(arr):
    A = max(arr)
    return A
arr = [5,6,1,7,2,9,4]
print(max_element(arr))


#3.
def sort_element(arr):
    A = arr[0]
    for i in arr:
        if i>=A:
            A = i
