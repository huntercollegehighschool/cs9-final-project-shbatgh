"""
Name(s): Sam Boccara
Name of Project: Hangman
"""

import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ['ant', 'baboon', 'badger', 'bat', 'camel', 'otter', 'fox', 'mouse', 'mule', 'spider', 'wombat', 'zebra']

guessProgress = []
guessNumber = 0
guessedLetters = []

while guessNumber < 8:
  if guessNumber == 0:
    answer = words[random.randint(0, len(words) - 1)]
    for i in range(len(answer)):
      guessProgress.append("_")

    guessNumber += 1
  
  print(HANGMANPICS[guessNumber - 1])
  print("".join(guessProgress) + " Guessed Letters: " + "".join(guessedLetters) + " Mistakes Left: " + str(8 - guessNumber))
  
  guess = input("Guess a letter: ")
  
  for i in range(len(answer)):
    if guess == answer[i]:
        guessProgress[i] = guess

  if guess not in answer:
    guessedLetters.append(guess)
    guessNumber += 1

  if "".join(guessProgress) == answer:
    print("Congratulations! You Won!")
    play_again = input("Do you want to play again (y/n)? ")

    if play_again == "n":
      break
    elif play_again == "y":
      guessNumber = 0
      guessProgress.clear()
      continue

  if guessNumber == 8:
    print("You lose. The answer was", answer)
      


#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
