# Find The largest Element of the Array



def findTheLargestElement(arr):
    result = arr[0]
    for i in range(len(arr)):
         result = max(result,arr[i])
    return result
arr= [-1,-4,-6,-3,-90,-2]#[1,6,78,3,2,9000,2344,45,5,56,67,54,5,7,56,53,54,435]
print(findTheLargestElement(arr))
