#print The duplicates value of array
# Program 1
def showDuplicates_value(arr):
    A= []
    B = []
    for i in arr:
        if i not in A:
            A.append(i)
        elif i not in B:
            B.append(i)
    return B
            
arr = [1,4,2,3,5,6,7,8,1,2,3]
print(showDuplicates_value(arr))

# program 2
def showDuplicates_value(arr):
    A= []
    B = []
    for i in arr:
        if i not in A:
            A.append(i)
        elif i not in B:
            B.append(i)
    return B
arr = []
n= int(input("Enter the Number for appending  value :"))
for i in  range(n+1):
   A =  int(input("Enter the array Element  here :") )
   arr.append(A)        

print("The Duplicates of array element = ",showDuplicates_value(arr))
