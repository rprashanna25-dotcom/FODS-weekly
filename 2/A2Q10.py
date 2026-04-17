import random  # To generate random dice roll

#  Guessing game
def dice_game():
    dice = random.choice([1, 2, 3, 4, 5, 6])  # Dice roll between 1 and 6
    
    # Ask the user to guess
    guess = int(input("Guess the dice value (1-6): "))
    
    # Check the guess
    if guess == dice:
        print(f"You guessed {guess}, dice rolled {dice} 😄")  # Correct guess
    elif abs(guess - dice) == 1:
        print(f"You guessed {guess}, dice rolled {dice} 😐")  # Guess off by 1
    else:
        print(f"You guessed {guess}, dice rolled {dice} You didn't get it")  # Wrong guess

# Run the game
dice_game()