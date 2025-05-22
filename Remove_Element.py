# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# 1.
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
           nums[k] = nums[i]
    return k
    
num = [2,3,45,21,3,2]
val = 3
removeElement(num,val)
print(nums)



# 2.
def removeElement(nums, val):
    k = []
    for i in range(len(nums)):
        if nums[i] != val:
            k.append(nums[i])
   return k
    
num = [2,3,45,21,3,2]
val = 3
removeElement(num,val)
print(nums)
