 #print the last digit og number 
# method 1
def returnlastdigit(n):
    if len(str(n)) > 1:
        ans = abs(n)%10
        print(ans)
        return
     # Print ans
    print(n)
returnlastdigit(-433)

# method 2 
def returnlastdigit(n):
    c = str(n)
    ans = c[-1]
    print(ans)
returnlastdigit(-433)
