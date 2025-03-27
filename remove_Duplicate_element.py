# Remove the Duplicate Element  of the array
# 1. Method
arr = [23,78,89,1,7,5,1,4,6,6,5,4]
A = set(arr)
S = list(A)
print(S)

# 2. Method
def remove_duplicate(arr):
    A = set(arr)
    S = list(A)
    return S
arr = [1,2,3,1,2,4,5,1,3,6,3,4,2,5,7,5,8,9,9]
print(remove_duplicate(arr))

# 3. Method

arr = [2,3,5,3]
if len(arr)<2:
    print(arr)
else:
    A = []
    for i in arr:
        if i not in A:
            A.append(i)
    print(A)

# 4.Method 


def remove_Duplicate_element(arr):
    if len(arr)<2:
        return arr
    else:
        A = []
        for i in arr:
            if i not in A:
                A.append(i)
        return A
arr = [2,5,8,1,6,1,4,2,7]
print(remove_Duplicate_element(arr))
