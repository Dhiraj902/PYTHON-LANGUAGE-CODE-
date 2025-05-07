# plush One in last element 

def plush_one(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        if nums[i] < 9:
            nums[i] += 1
            return nums
        nums[i] = 0
    return [1] + [0]*n
l= []
nums = int(input("Enter the number "))
for i in range(nums):
    A = int(input())
    l.append(A)
result = plush_one(l)
print(result) 
