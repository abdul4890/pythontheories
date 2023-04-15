import random

print(''' 1: roll the dice 2. To exit ''')
user = int(input('enter the number:'))
if user == 1:
    number = random.randint(1,6)
    print(number)
else:
 print('exit')