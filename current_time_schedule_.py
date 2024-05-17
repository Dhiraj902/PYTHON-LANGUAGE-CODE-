#wap to print current time
mport time
t = time.ctime()
print(t) 

#wap to print current time and second schedule..
mport time 

current_time = time.strftime('%H:' '%M :' '%S ')

current_hours = time.strftime('%H')

if(11>=int(current_hours) ):
     print("Good Morning")

elif(11<int(current_hours) and 18> int(current_hours)):
     print("Good Afternoon")

elif(17< int(current_hours) and 19>int(current_hours)):
     print("Good Evening")

else:
     print("Good Night")

while True:
   
  current_time = time.ctime()
    
  print("Currennt Time :", current_time ,end='\r')
    time.sleep(1)



#wap to print current time and second
import time

while True:
   
  current_time = time.ctime()
   
print("Currennt Time :", current_time ,end='\r')
    
time.sleep(1)

