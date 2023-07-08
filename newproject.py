#python program to check maximum of 2 numbers
def palin(s):
    return s == s[::-1]

s = "civic"
a = palin(s)

if a:
    print("yes")
else: 
    print("no")



