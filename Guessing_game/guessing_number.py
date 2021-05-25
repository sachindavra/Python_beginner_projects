from random import randint


name = input("Enter your name: ").capitalize()
print(f"Welcome to the number guessing game {name}!")
numbers = [12, 45, 58, 67, 77, 89, 94]
index = randint(0, (len(numbers) - 1))
number = numbers[index]
guess = int(input("Guess any number between 1 to 100: "))
count = 10


def playagain():
    user_input = input("Do you want to play again? (Yes/No): ").lower()
    if user_input == "yes":
        global index, number, guess, count
        index = randint(0, (len(numbers) - 1))
        number = numbers[index]
        guess = int(input("Guess any number between 1 to 100: "))
        count = 10


while count > 0:
    if guess < number:
        count -= 1
        print("Hint: your guess is less than the number.")
        print(f"You have {count} guesses left.")
        guess = int(input("Try again: "))
    elif guess > number:
        count -= 1
        print("Hint: your guess is greater than the number.")
        print(f"You have {count} guesses left.")
        guess = int(input("Try again: "))
    else:
        print("\nYou won!. You have guessed it right!")
        playagain()
        break

    if count == 0:
        print(f"You loose. Your number was {number}.")
        playagain()
