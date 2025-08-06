# Remove The Duplicates Element From Array


def remove_duplicates(arr):
    j= 0
    key_pair = {}
    for i in range(len(arr)):
            key_pair[arr[i]] = 0
    j = 0
    for k in key_pair:
        arr[j] = k
        j+=1
        
    return j
arr= [1,2,3,4,53,1,2,3,6,9,6,7,0,6,7]
print(remove_duplicates(arr))
