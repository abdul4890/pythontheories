number = int(input('enter the number:'))
if number<2:
    print("Not prime")
else:
        for i in range(2,number):
            if number%i== 0:
             print("not prime")
            break
        else:
            print("number is prime")

