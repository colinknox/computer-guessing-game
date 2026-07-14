import random

computer_guess_count = 0

while True:
    try:
        user_number = int(input("Please input a number between 1 and 100 for the computer to guess: "))
        break
    except ValueError:
        print("Invalid input.")

print(f"The computer must guess {user_number}!")

while True:
    computer_guess = random.randint(1, 100)

    print(f"The computer guesses {computer_guess}.")

    if computer_guess_count == 5:
        print("Computer ran out of turns! You win! :)")
        break

    if computer_guess > user_number:
        print("Too high!")
        computer_guess_count += 1
    elif computer_guess < user_number:
        print("Too low!")
        computer_guess_count += 1
    else:
        print("Computer guessed correctly! You lose! :(")
        break


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
