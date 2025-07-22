# Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

    def countFreq(arr, target):
        A = 0
        for i in range(len(arr)):
            if arr[i]== target:
                A += 1
        return A

    arr = [1,2,3,4,45,6,4]
    target = 2
    print(countFreg(arr,target))
        
