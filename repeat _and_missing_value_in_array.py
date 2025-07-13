"""Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].

Examples:

Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and smallest positive missing number is 1.
Input: arr[] = [1, 3, 3] 
Output: [3, 2]
Explanation: Repeating number is 3 and smallest positive missing number is 2.
Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5."""



##
def repetevalue(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            repeat = arr[i]
            break  
    z = list(set(arr))
    A = len(z)+1
    a = (A*(A+1))//2
    s = a - sum(z)
    return [repeat,s]
    
arr = [1,2,4,4]
repetevalue(arr)


## 
def repetevalue(arr):
    list1 = []
    list2 = []
    for i in arr:
        if i  not in list1:
            list1.append(i)
        else:
            list2.append(i)
            
        
    z = list(set(arr))
    A = len(z)+1
    a = (A*(A+1))//2
    s = a - sum(z)
    list2.append(s)
    return list2
    
arr = [1,2,4,4]
print(repetevalue(arr))
    


