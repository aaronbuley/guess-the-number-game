# Guess a number game
#Add feature to check if the input number was between 1-100
#Add levels to the game to make it more exciting

from random import randint  #To generate a random number

def game():
    rand_number = randint(0,100)   #Generates a random number
    print("\nI have selected a number between 1 to 100...")
    print("You have 6 chances to guess that number...")
    i = 1
    while i<7:  #6 Chances to the user
        user_number = int(input('Enter your number: ')) 
        if user_number < rand_number:
            print("\nMy number is greater than your guessed number")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif user_number > rand_number:
            print("\nMy number is less than your guessed number")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif user_number == rand_number:
            print("\nYou have guessed the correct number! Congratulations!!!")
            break
        else:
            print("This is an invalid number. Please try again")
            print("you now have " + str(6-i)+ " chances left" )
            continue
    print("Sorry you lost the game!!")
    print("My number was = " + str(rand_number))

def main():
    game()
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
        else:
            break
main()
print("\nEnd of the Game! Thank you for playing!")
