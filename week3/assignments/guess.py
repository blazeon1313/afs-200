myWord = "VICTORIOUS"
copyWord = "myWord"

wordBoard = ["_"]*len(myWord)
wordBoard
guessedLetters = []

def showBoard():
    print(" ".join(wordBoard))
    
def checkGuess(guess, myWord, wordBoard):
    index = myWord.find(guess)
    while index != -1:
        if guess in myWord:
            index = myWord.find(guess)
            removed_character = '*'
            myWord = myWord[:index]+removed_character+myWord[index+1:]
            wordBoard[index] = guess
        else:
            index = -1
    return (myWord, wordBoard)

def win_check():
    for i in range(0, len(wordBoard)):
        if wordBoard[i] == '_':
            return -1
    return 1

print("Can you guess the secret word?")

num_turns = 9

while (num_turns):
    showBoard()
    guesses = input("Guess a letter: ").upper()

    if guesses in myWord:
        myWord, wordBoard = checkGuess(guesses, myWord, wordBoard)
        guessedLetters.append(guesses)
    elif guesses in guessedLetters: 
        print("You already guessed that letter " +guesses)
        num_turns = num_turns
    else:
        print("Sorry that letter is not in the word.")
        num_turns = num_turns-1
        guessedLetters.append(guesses)

    if win_check() == 1:
        num_turns = 0
        print("Congratulations you guessed the word! ")
    elif num_turns == 0:
        print("You have run out of guesses. GAME OVER!!")
    
    print("You have " +str(num_turns)+ " turns left.")
    print()