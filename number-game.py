# Guess a number game
from random import randint  #To generate a random number

rand_number = randint(1,100)   #Generates a random number

print("I have selected a number between 1 to 100...")
print("You have 6 chances to guess that number...")

i = 1
while i<7:  #6 Chances to the user
    user_number = int(input('Enter your number: ')) 
    if user_number < rand_number:
        print("My number is greater than your guessed number")
        print("you now have " + str(6-i)+ " chances left" )
        i = i+1
    elif user_number < rand_number:
        print("My number is less than your guessed number")
        print("you now have " + str(6-i)+ " chances left" )
        i = i+1
    else:
        print("You have guessed the correct number! Congratulations!!!")
        break

print("\nEnd of the Game! Thank you for playing!")
