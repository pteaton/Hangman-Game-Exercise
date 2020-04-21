print('Hello, HW 20')

import random
from words import words


# print(words)


class Word():
  def __init__(self, word):
    self.word = word

  def display_word(self):
    blank_word = ""
    for char in self.word:
      blank_word += " _ "

    print(blank_word)

hello = Word("hello")
print(hello.word)
hello.display_word()

# GAME 
playing = True
lives = 6
user_guessed_correctly = False
letters_guessed = []

print("\n\n\n\nHey! Welcome to Hangman! Lets get started :) Type 'quit' at any time to exit.")

while playing:
  user_input = input(f"\nYou have {lives} lives. \n\n{this_rounds_word.display_word_method()} \n\nLetters guessed so far: {letters_guessed}\n\nMake a new guess. ")
  if user_input in letters_guessed:
    print('\n\nguess something you have\'t yet, silly!')
  elif user_input == "quit":
    print('\n\nokay goodbye :( ')
    playing = False
  elif len(user_input) > 1:
    print('\n\nOnly one letter at a time please!')
  else:
    for word in split_word:
      if user_input == word['letter']:
        word['guessed'] = True
        user_guessed_correctly = True
    letters_guessed.append(user_input)

    if user_guessed_correctly:
      if " _ " not in this_rounds_word.display_word_method():
        print(f"\n\nYOU WIN! The word was {this_rounds_word.word}!")
        playing = False
      else:
        print("\n\nYou Got One!")
      user_guessed_correctly = False
    else:
      if lives < 1:
        print(f'\n\nu LOSE! The word was {this_rounds_word.word} :(')
        playing = False
      else:
        print('\n\nNope :/ Try Again!')
        lives -= 1