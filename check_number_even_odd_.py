#wap to check the number of even or odd without function ..

number = int(input("Enter the number......"))
if (number%2==0):
 print("the number is even.... ")
else:
 print("the number is odd...")


#wap to check number is even or odd  by using function 


def even_odd(num):
    if num%2==0:
        print("The number is even:",num)
    else:
        print("the number is odd:",num)
even_odd(3)

#wap to check number is even or odd  by using function (by user)
def even_odd():
    if(num%2==0):
        print("the number is even:",num)
    else:
        print("The number is odd:",num)
num = int(input("Enter the number here:"))
even_odd()
        
