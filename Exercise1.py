# Guess number game
# Computer will detect if the number is too low or high than the actual number
# Store the actual number in a variable
#4 you have to finally tell how many attempts did you take to guess the number

# Declaring variables

actual_number = 56
attempts = 0
while True:
    attempts += 1
    guess = int(input("guess the number: \n"))
    if guess<actual_number:
     print("your guess was too low")
    elif guess>actual_number:
     print("your guess was too high")
    else: 
      print(f"you guessed the number in {attempts} attempts")
     
      
  

    