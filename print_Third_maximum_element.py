# print the third maximum  lellement of array or List
def thirdMax( nums):
        A = list(set(nums))
        A.sort(reverse=True)
        if len(A)>= 3:
            print(A[2])
        else:
            print(A[0])
nums= [-1,0,2]
thirdMax(nums)
