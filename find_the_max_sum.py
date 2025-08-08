# Kadane's Algorithm 
# Find The max Sum using the kadane's Algorothm





def max_sum(arr):
    current_sum = 0
    max_Sum = float("-inf")
    for i in range(len(arr)):
        current_sum += arr[i]
        max_Sum = max(max_Sum,current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_Sum
arr = [-2,-4]
print(max_sum(arr))
