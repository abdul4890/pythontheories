string = str(input("enter the word:"))
temp = string[::-1]
if string == temp:
    print("palindrom")
else:
    print("not palindrome")