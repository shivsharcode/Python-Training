
def guessGame():
    print("Guess the magic number")
    turn = 0

    while not (turn == 3):
        guess = int(input("Guess: "))
        if guess == 9:
            print("You Won !")
            return
        turn += 1

    print("Sorry you failed")
    return


print("\n--Guess Game--")
guessGame()
