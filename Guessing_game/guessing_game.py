from random import sample, randint

name = input("Enter your name: ")
print(f"Hello {name}!, welcome to the guessing game.")
words_list = ["output", "sunset", "application", "message", "python", "programming"]
chances = 10
index = randint(0, (len(words_list) - 1))
words = words_list[index]
indexes = sample(range(0, len(words)), 3)
guesses = ""  # what user have guessed
play = "Yes"

for i in indexes:
    guesses += (words[i])


def playAgain():
    global play
    play = input("Do you want to play again? (Yes/No): ").lower()
    if play == "yes":
        global chances, words, guesses
        chances = 10
        index = randint(0, (len(words_list) - 1))
        words = words_list[index]
        indexes = sample(range(0, len(words)), 3)
        guesses = ""
        for i in indexes:
            guesses += (words[i])

        play = "Yes"


while play == "Yes":
    while chances > 0:
        won = True
        for word in words:
            if word in guesses: # The person has guesses
                print(word, end=" ")
            else:
                print("_", end=" ")
                won = False
        if won:
            print(f"\nCongratulations {name}, you have won the game.")
            print(f"Your score is {chances*10}.")
            playAgain()
            break

        # Now take a guess from the user.
        guess = input("\nEnter any character: ")
        guesses += guess
        if guess not in words:
            chances -= 1
            print("\nWrong guess.")
            print(f"You have {chances} chances left.")

            if chances == 0:
                print("\nyou lose")
                playAgain()
                break

