# Remove The Duplicate String From The String
def removeDups(str):
    A = ''
    for i in range(len(s)):
        if s[i] not in A:
            A += s[i]
    return A
s = "Dheeraj"
print(removeDups(s))
