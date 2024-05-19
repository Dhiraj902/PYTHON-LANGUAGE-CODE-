#wap to calculate the sphere of volume without using function:
redius = float(input("Enter the redius :"))

print("The  sphere of volume:",(4/3*3.14*redius**3))



#wap to calculate the sphere of volume by using function:
def sphere_volume():
   
  return (4/3*3.14*redius**3)

redius= float(input("Enter the value of redius:"))

print("The sphere of volume:",sphere_volume())


#wap to calculate the sphere of volume by using function:
def sphere_volume(redius):
    
  return 4/3*3.14*redius**3

print(sphere_volume(2))
