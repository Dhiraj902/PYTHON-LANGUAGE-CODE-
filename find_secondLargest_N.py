# find the second largest element in to array
def second_largest_N(arr):
    set1 =  set(arr)
    List1 = list(set1)
    if len(List1)<2:
        return -1
    List1.sort()
    return List1[-2]
arr = [10,5,10,45,20]
print(second_largest_N(arr))
