import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Set the number of chances to 10
chances = 10

# Loop for the number of chances
for i in range(chances):
    # Get user input
    guess = int(input("Guess the number between 1 and 100: "))
    # Check if the guess is too low, too high, or correct
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        break
# If the guess is correct, print the number of guesses and the correct number
if guess == number:
    print("You guessed the number in", i+1,"tries. The correct number is", number)
else:
    print("Sorry, you did not guess the number. The correct number was", number)