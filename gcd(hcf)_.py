1.#wap to find the hcf(gcd) of value:
x = int(input("Enter the first value:"))

y = int(input("Enter the second number:"))

for i in range(x,0,-1):
   
    if(x%i==0 and  y%i==0):
      
      break

print(f"The HCF(gcd) of {x} and {y} :",i)



1.#wap to find the hcf(gcd) of value usinf math function:
import  math

x = int(input("Enter the first value:"))

y = int(input("Enter the second value:"))

a = math.gcd(x,y)

print(f"The HCF(gcd) of {x} and {y} :",a) 


2.#wap to find the hcf(gcd) of value usinf math function:
from  math  import lcm

x = lambda a,b: (a*b)//lcm(a,b)

a = int(input("Enter the value:"))

b = int(input("Enter the value:")) 

print(f"The HCF(gcd) of {a} and {b} :",x(a,b)) 



2.#wap to find the hcf(gcd) of value:
x = int(input("Enter the first  value:"))

y = int(input("Enter the second  value:"))

gcd = min(x,y)

n = gcd

while True:
    
    if(x%n==0 and y%n==0):
    
     break
   
    n-=1

print(f"The HCF(gcd) of {x} and {y} :",n)



3.#wap to find the hcf(gcd) of value:
x = int(input("Enter the  first value :"))

y = int(input("Enter the second value:"))

for i in range(2,x*y-1):
    
    if(x%i==0 ):
     
        t =i
      
        for j in range(i,x*y-1):
        
          if(y%i==0):
        
           break
       
        if(t == j):
        
          print(f"The HCF(gcd) of {x} and {y} :",i)
         
          break



4.#wap to find the hcf(gcd) of value:
x = int(input("Enter the first value:"))

y = int(input("Enter the first value:"))

for i  in range(x if x<y  else y,0,-1):
    
   if(x%i==0 and y%i==0):
     
      print(f"The HCF(gcd) of {x} and {y} :",i)
    
   break
