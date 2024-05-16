#wap to check the maximum value using max function
a = 2
b = 3
print("the min value is = ",max(a,b))


#wap to check the maximum value without  using max function

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
if(num1>num2):
    print("The maximum num of:",num1)
else:
    print("The maximum number of:",num2)
 
 
 
1. #wap to check the maximum value  using  function  
def max(a,b,c):
    if(a>b and a>c):
        print("The maximum number is:",a)
    elif(b>c):
        print("The maximum number is:",b)
    else:
        print("The maximum number is:",c)
        return a,b,c
    
max(10,29,30)


2.#wap to check the maximum value  using  function  
def max():
    if(a>b and a>c):
        print("The maximum number is:",a)
    elif(b>c):
        print("The maximum number is:",b)
    else:
        print("The maximum number is:",c)
        return a,b,c
a= int(input("Enter the first  number:"))
b= int(input("Enter the second   number:"))
c= int(input("Enter the  third number:"))
max()
