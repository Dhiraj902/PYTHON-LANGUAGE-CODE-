# Reverse the wards 

def reverse(S):
    L = S.split()
    L.reverse()
    A = ' '.join(L)
    return A

S = " i like this program very much "  # much very program this like i
print(reverse(S))
