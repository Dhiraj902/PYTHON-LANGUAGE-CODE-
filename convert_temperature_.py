#wap to convert celsius_to_fah  temp without function..
celsius_to_fah = int(input("Enter the value:"))

fah = (celsius_to_fah *1.8)+32

print(fah)


#wap to convert celcius to fahrenheit temp using function...

def cel_to_fah(celsius):

    return(celsius * 1.8)+32


cel  = int(input("Enter the celsius value....(to convert the fahrenheit..)"))

print("the "+str(cel)+"' celsius is = ",cel_to_fah(cel),"fahrenheit.")



#wap to convert fah_to_celsius convert temp without function..

fah_to_celsius = int(input("Enter the value:"))

celcius = ( fah_to_celsius -32)/1.8

print(celcius)


# fahrenheit to celcius convert temp using function.....

def fah_to_cel(fahrenheit):

    return(fahrenheit -32 )/1.8

fah  = int(input("Enter the fahrenheit value....(to convert the celsius...)"))

print("the "+str(fah)+"' fahrenheit is = ",fah_to_cel(fah),"celsius.")



