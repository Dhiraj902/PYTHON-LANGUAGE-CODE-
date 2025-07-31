# Check The array element is Palindrom or not 


def isPalinArray(arr):
    A = 0
    for i in arr:
        S = str(i)
        if S[::-1]==S:
            A +=1
    if A == len(arr):
        return True
    False
