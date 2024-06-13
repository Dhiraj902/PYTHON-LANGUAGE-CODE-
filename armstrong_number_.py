#WAP to check the armstrong number:
num = int(input("Enter the number  "))

order = len(str(num))

print("The order is the  number = ", order)

sum =0

temp = num

while temp>0:
 
  digit = temp%10
 
cube = digit**order
 
sum = sum + cube
 
temp//=10

if num == sum:
 
  print("this is the armstrong  nunmber: ")

else:
 
  print("not armstrong number:")
 
