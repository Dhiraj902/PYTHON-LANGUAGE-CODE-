#wap to check the number of prime or not prime. without using function ..
num = int(input("Enter the  number:"))
for i in range(2,num+1):
    if(num%i==0):
        break
if(i==num):
    print("The number is prime.",num)
else:
    print("The number is not prime:",num)

(1)#wap to check the number of prime or not prime using function
def prime(num):
    if num<=1:
        return False
    for i in range(2,num+1):
        if num%i==0:
            break
    if(num==i):
        return True
    else:
        return False
print(prime(1))


(2)#wap to check the number of prime or not prime using function
def prime(num):
    if num<=1:
        print("The number is not prime:",num)
        return  
    for i  in range(2,num+1):
        if(num % i == 0 ):
            break
    if(num == i):
        print("the number is peime:",num)
    else:
        print("The number is not  prime:",num)
        
num = int(input("Enter the number for check prime or not prime:"))
prime(num)
