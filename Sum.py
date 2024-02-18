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

# #programme to write a palindrome
# a = input("enter the word ")

# while True:
#  if a == a[::-1]:
#    print("it is a palindrome")
#  else:
#     print("it is not a palindrome")
#  break

# Programme to check the number's interval
# num1 = 10
# num2 = 20

# for i in range(num1, num2 + 1, 2):
#     print(i)

# #programme to check multiplication of 4
# num1 = int(input("enter the number"))
# for i in range(1,10):
#  print(num1*i)

#programe to generate random character
# import random
# uppercase1=chr(random.randint(66,90))
# uppercase2=chr(random.randint(66,90))
# a = [uppercase1,uppercase2]
# j = "".join(a)
# print(j)

# import random

# def shuffle(string):
#     tempList = list(string)
#     random.shuffle(tempList)
#     return ''.join(tempList)

# uc=chr(random.randint(65,90))
# lc=chr(random.randint(65,90)).lower()
# dig=str(random.randint(0,10))

# password = uc + lc + dig
# a = shuffle(password)
# print(a)

# import pywhatkit
# pywhatkit.sendwhatmsg("+918402835389", 
#                       "this is an automated msg by razi again", 
#                       19,12)

#python programme to open a website
# import webbrowser

# #take thr url
# url = "https://www.facebook.comW/"

# #use the opne default methof using the module
# webbrowser.open(url)

#programme using fucntions
# def sum(a,b):
#     print(a + b)
# sum(2,44)

#programme to write using function to find square root
# def square_(num):
#     result = num * num
#     return result

# square = square_(9)
# print("squaree is", square)

# from time import sleep
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get("https://www.instagram.com/")

# sleep(11)
# # browser.close()
# def palindrome(s):    
#     return s == s[::-1]

# s = "mnoo"
# ans = palindrome(s)

# if ans:
#     print("yes")
# else:
#     print("no")

#Creating a dictionary


# fullname = {
#     "Razi" : "Ansari",
#     "Israr" : "Ansari",
#     "Adil" : "Ansari",
#     "Rishan" : "Ansari"
# }
# print(fullname)
