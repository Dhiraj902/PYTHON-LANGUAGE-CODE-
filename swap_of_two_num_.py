(1)#wap to  print the swapping of two number without using function:

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
temp = num1
num1 = num2
num2 = temp
print("The first number of after swapping :",num1)
print("Tthe second number of after swapping:",num2)



(2)#wap to  print the swapping of two number without using function:
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num1,num2 = num2,num1
print("The first number of  after swapping :",num1)
print("the second number of after swapping:",num2)



(1)#wap to  print the swapping of two number by using function:
def swap(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1,num2
print("the number  of ofter swapping",swap(12,23))



#wap to  print the swapping of two number by using function:
def swap(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1,num2
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print("the number  of ofter swapping",swap(num1,num2))



(3)#wap to  print the swapping of two number without using function and temporary variable:
num1 = int(input("Enter the  first number:"))
num2 = int(input("Enter the second number:"))
num1 = num1+num2
num2 = num1-num2
num1 = num1- num2
print("the first number of after swapping :",num1)
print("THe second number of after swapping :",num2)
