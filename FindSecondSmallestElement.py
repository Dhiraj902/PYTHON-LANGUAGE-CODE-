# find the second  smallest element from the array


def findSecondsmallest(arr):  
    B = list(set(arr))
    B.sort()
    S = min(B)
    D = [S]
    if len(B)<2:
        return [-1]
    elif len(B)==2:
        return B
    else:
        D.append(B[1])
    return D
arr=[678,67]
print(findSecondsmallest(arr))
