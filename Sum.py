#python program for loop

#creating a dictonary
# country_couples = {
#     "United States" : "Washington DC",
#     "India" : "New Delhi",
#     "Egypt" : "Cairo",
#     "Pakistan" : "Islamabad"
# }
# #creating a for loop
# for capitals in country_couples:
#     print(capitals)

# #Creating a list
# lang = ["java", "c++", "python"]
# for language in lang:
#     print(lang)

#Creating a tupple
# lang = ("python", "java", "c++")
# for language in lang:
#     print(language)

# #Creating a new string
# a = "python is the best language"
# print(a)


# #Programme to reverse a string
# Str = "this needs to be reversed"
# print("".join(reversed(Str)))

# #creating a prime number programme

# number = int(input("enter the number:"))
# if number == 1:
#     print(num, "is not a prime number")
# elif number > 1:
#  for i in range(2, number):
#     if (number % i) == 0:
#         print(number, "is not a prime number")
#         break
#  else:
#     print(number, "its a prime number")
        
# #Python programme to check the largest of 3 numbers
# num1 = int(input("enter number 1:"))
# num2 = int(input("enter number 2:"))
# num3 = int(input("enter number 3:"))

# if (num1 >= num2) and (num1 >= num3):
#     print("num 1 is largest")
# elif (num2 >= num1) and (num2 >= num3):
#         print("num 2 is largest")
# else:
#             print("number 3 is largest")

#programme to write a palindrome
a = input("enter the word ")

while True:
 if a == a[::-1]:
   print("it is a palindrome")
   break

else:
    print("it is not a palindrome")


