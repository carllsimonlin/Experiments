# Readme Guide

## Introduction

This is a Python program that generates a random number between 1 and 100 and asks the user to guess the number within 10 tries.


## How to use the program

1.  Open your terminal or command prompt.
2.  Navigate to the directory where the program is saved.
3.  Run the command `experiment_3.py` to start the program.
4. The program will generate a random number between 1 and 100.
You have 10 tries to guess the number.
5. After each guess, the program will tell you if your guess is too high, too low, or correct.
6. If you guess the number correctly within 10 tries, the program will tell you the number of tries it took you to guess the number.
7. If you do not guess the number correctly within 10 tries, the program will reveal the correct number.

## Code Explanation
The code uses the random module to generate a random number between 1 and 100. It then sets the number of chances to 10 using the chances variable.

The program then uses a for loop to loop for the number of chances. Inside the loop, the program gets user input using the input() function and checks if the guess is too low, too high, or correct using if-elif-else statements.

If the guess is correct, the program uses the break statement to exit the loop. After the loop, the program checks if the guess is correct using an if-else statement. If it is, the program prints the number of guesses and the correct number. If it's not, the program prints the correct number.