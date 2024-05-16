
#WAP find the minimum of two number using min function....

a = 2
b = 3
print("the min value is = ",min(a,b))


#WAP find the minimum of two number  without using min function....
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
if(num1<num2):
    print("The minimum num of:",num1)
else:
    print("The minimum number of:",num2)
 
 
 

1.#WAP find the minimum of two number by  using  function....   
def min(a,b,c):
    if(a<b and a<c):
        print("The minimum number is:",a)
    elif(b<c):
        print("The minimum number is:",b)
    else:
        print("The minimum number is:",c)
        return a,b,c
    
min(10,29,30)



2.#WAP find the minimum of two number by  using  function....
def min():
    if(a<b and a<c):
        print("The minimum number is:",a)
    elif(b<c):
        print("The minimum number is:",b)
    else:
        print("The minimum number is:",c)
        return a,b,c
a= int(input("Enter the first  number:"))
b= int(input("Enter the second   number:"))
c= int(input("Enter the  third number:"))
min()
