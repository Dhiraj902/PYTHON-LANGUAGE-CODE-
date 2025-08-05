# Smallest Positive Missing
"""
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too
"""
def findMissingValue(arr):
    for i in range(1,len(arr)+2):
        if i not in arr:
            return i 
arr =[ 1 ,2,3,4,5,6,7]
print(findMissingValue(arr))
