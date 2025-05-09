#  Simple calculator in Python

# Python Program to create a simple Calculator 
# 3 Step to build calculator Program

#   1. Function For Operations
#   2. user input
#   3. print result

# Step -1
#  Function to add two numbers 
def add(num1 ,num2):
    return num1 + num2

#  Function to sunbtract two number
def sub(num1, num2):
    return num1 - num2

#  Function to multiply Two number
def mul(num1,num2):
    return  num1* num2

# Function to division of Two number

def division(num1,num2):
    return num1 / num2


#  Function to find the  mean or Average 

def avg(num1 , num2):
    return (num1+num2)/2

# Step - 2
while True:
    print(""" \n -> Plese Select the Operation :\n 
                1. Addition 
                2. Substraction
                3. Multiplication
                4. Divition
                5. Avarage \n
          """)
    select = int(input("Enter the number 1/2/3/4/5:"))
    num1 = int(input("Enter the  first value here : "))
    num2 = int(input("Enter the second Value here : "))
    
    # Step - 3
    
    if select == 1:
        print(f"The sum of {num1} and {num2} is :",add(num1,num2))
    
    elif select == 2:
        print(f"The subtraction of {num1} and {num2}  is :",sub(num1,num2))
    
    elif select == 3:
        print(f"The multiplication of {num1} and {num2} is : ", mul(num1,num2))
    
    elif select == 4:
        print(f"The Division of {num1} and {num2} is : ",division(num1,num2))
    elif select == 5:
        print(f"The Avarage of {num1} and  {num2} is : ",avg(num1,num2))
    else:
        print(""" this is invalid Input :->
                Plese Enter the correct input ->
              """)
