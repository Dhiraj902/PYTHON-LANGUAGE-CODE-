#wap to find the lcm using math function:
import math 

x = math.lcm(4,6)

print(x)



1.#wap to find the lcm  of value:
x = int(input("Enter the  first value :"))

y = int(input("Enter the second value:"))

for i in range(2,x*y+1):
    
  if(i%x==0 ):
        
    t =i
       
    for j in range(i,x*y+1):
         
      if(j%y==0):
          
        break
        
        if(t == j):
          
          print(f"The LCM {x} and {y} :",i)
          break



2.#wap to find the lcm of value:
x = int(input("Enter the  first value :"))

y = int(input("Enter the second value:"))

for i in range(1,x*y+1):
    
  if(i%x==0 and i%y==0):
    
    break

print(f"The LCM {x} and {y} :",i)




2.#wap to find the lcm using math function:
from  math  import gcd

x = lambda a,b: abs(a*b)//gcd(a,b)

a = int(input("Enter the value:"))

b = int(input("Enter the value:")) 

print(x(a,b)) 



3.#wap to find the lcm  of value:
x = int(input("Enter the first  value:"))

y = int(input("Enter the second  value:"))

lcm = max(x,y)

n = lcm

while True:
   
  if(n%x==0 and n%y==0):
        
    break
    
  n+=lcm
   
print(n)
    


4.#wap to find the lcm of value:
x = int(input("Enter the first value:"))

y = int(input("Enter the first value:"))

for i  in range(x if x<y  else y,x*y+1):
    
  if(i%x==0 and i%y==0):
     
    print(i)
      
    break
