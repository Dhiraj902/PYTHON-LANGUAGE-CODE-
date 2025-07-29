# Check the k is equal to the sum of triple element of the array
# is equal then return True else return  False


def hasTripletSum( arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]  == target:
                    return True
    return False
arr =[1, 4, 45, 6, 10, 8]
k = 13
print(hasTripletSum(arr,k))
