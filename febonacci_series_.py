
#WAP to print the febonacci series .

num = int(input("Enter the number:"))
n1 = 0
n2 = 1
if(num == 1):
   print(0)

else:

 print(n1)
 print(n2)
 for i in range(2,num):
   
   c = n1+n2
   n1 = n2
   n2 = c
   print(c)


#WAP to print the febonacci series using recursion .        
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input("Enter the number: "))
for i in range(num):
    print(fibonacci(i))
