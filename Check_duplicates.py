# Check Duplicates Value in the  array

def check_duplicate(arr):
    if len(arr) == len(set(arr)):
        return False
        
    return True
arr = [2,14,18,22,22]
print(check_duplicate(arr))
