#  FInd The Equlibrium point in The Array
# Brute Force method

def equlibrium_point(arr):
    for i in range(len(arr)):
        left_sum  = 0
        right_sum = 0
        for j in range(0,i):
            left_sum +=arr[j]
        for k in range(i+1,len(arr)):
            right_sum  += arr[k]
        if left_sum == right_sum :
            return i
    return -1
arr = [1,2,0,3]#[12,34,34,5,6,7,8,90]
print(equlibrium_point(arr))
