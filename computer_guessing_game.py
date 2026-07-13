computer_guess_count = 0

try:
    user_number = int(input("Please input a number between 1 and 100 for the computer to guess: "))
except ValueError:
    print("Invalid input.")

# If input is invalid:
    # Print "Input is invalid"
# Loop
    # Display number user picked so user remember what they typed
    # Computer guesses number
    # If number too high
        # Print "Computer guessed too high!"
    # If number too low
        # Print "Computer guessed too low!"
    # If computer guesses == 5:
        # Print "Computer ran out of turns! You win! :)"
        # break
    # Else
        # Print "Computer guessed correctly! You lose! :("
        # break
