print('Hello, HW 20')

from words import words
print(words)

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




# while playing:
#   user_input = input(" This is hangman! Make a guess now")
#   if user_input == 