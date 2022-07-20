number = 50
guess_count = 5
while True:
    guess = int(input("Enter the number : "))
    if number>guess:
        print("Enter a larger number.")
        guess_count -= 1
        print(f"You have {guess_count} guesses left.")
    elif number<guess:
        print("Enter a smaller number.")
        guess_count -= 1
        print(f"You have {guess_count} guesses left.")
    elif number==guess:
        print("Congratulatons.")
        break

    if guess_count == 0:
        print("You are out of guesses.")
        print("Try Again Next time.")
        break