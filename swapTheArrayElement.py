# Swap the araay Element 

def swapElement(arr):
    for i in range(len(arr)-2):
    
        temp = arr[i]
        arr[i] = arr[i+2]
        arr[i+2]= temp
    return arr 
arr = [1,2,8,7,6,49,1,68,28,65,3]
k = 3
print(swapElement(arr))
