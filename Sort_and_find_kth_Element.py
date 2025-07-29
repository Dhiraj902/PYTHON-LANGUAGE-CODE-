# Sort The aray Element 
# Find the kth Element



def kthSmallest(arr,k):
    A = 0 
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
      
    for i in range(len(arr)):
        A +=1
        if A == k:
            
            return arr[i]
arr =[ 14, 17, 18 ,16, 9, 12, 8 ,10 ,7 ,3, 5, 6, 13, 4, 2, 15, 1, 11]
k = 5
print(kthSmallest(arr,k))
print(arr)
