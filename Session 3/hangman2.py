import random
# a list of words
word = ["hangman", "pycharm", "python", "congratulations"]

# creating a random index to choose a word from the list
rand_index = random.randint(0, len(word)-1)

# creating the hangman
text = ""
for letter in word[rand_index]:
    text += "-"

# number of the guesses (number of letters of the chosen word)
guess = len(word[rand_index])

# the game
while guess != 0:
    # printing the hangman for user
    print(text)
    # getting a letter
    letter = input("Enter A letter: ").lower()
    # check to be sure user didn't enter a word
    if len(letter) != 1:
        continue
    # the position of the entered letter in the chosen word. it'll change to the next occurrence if it's available
    index = 0
    # if the letter was found then it wouldn't count as a wrong guess (it wouldn't reduce the number of guesses)
    flag = False
    # searches for the letter in the chosen word.
    while index != -1:
        index = word[rand_index].find(letter, index)
        if index != -1:
            flag = True
            # convert the chosen word to a list because apparently in python strings are immutable.
            temp = list(text)
            # changing the '-' with the found letter
            temp[index] = letter
            # converting the chosen word back to a string
            text = "".join(temp)
            # changing the index to avoid getting stuck in the loop
            index += 1
        # if not found break this loop go for another letter
        else:
            break
    # checking if user has won
    if text == word[rand_index]:
        print("Noice, you guessed it right. it was " + word[rand_index])
        break
    if not flag:
        guess -= 1

# checking if user has lost
if guess == 0 and text != word:
    print("You've lost soldier, better luck next time.")
