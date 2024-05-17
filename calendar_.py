#wap to print calendar
import calendar

y = int(input("enter year: "))

m = int(input("enter month: "))

calendar  = calendar.month(y,m)

print(calendar)



#wap to print calendar using function
import calendar

def print_month_calendar(year, month):
    try:
        
        month_calendar = calendar.month(year, month)
        
        print(month_calendar)
    
    except IndexError:
        
        print("Invalid month. Please enter a month between 1 and 12.")
    except ValueError:
        
        print("Invalid year. Please enter a valid year.")


try:
   
    y = int(input("Enter year: "))
    
    m = int(input("Enter month: "))
    
    print_month_calendar(y, m)

except ValueError:
   
    print("Invalid input. Please enter numeric values for year and month.")




