string = input("Enter the input")
vowels = 0
for i in string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
     vowels = vowels + 2
    print("the number of vowels are:")
    print(vowels)
