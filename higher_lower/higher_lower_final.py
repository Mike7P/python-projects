from art import logo
from art import vs
from game_data import data
from random import randint
from replit import clear

def winner(a, b):
  if a > b:
    return 'a'
  else: return 'b'
def game():
  print(logo)

  selectionA = []
  selectionB = []
  score = 0
  game_end = False

  random_numA = randint(1, 50)
  selectionA = data[random_numA]

  nameA = (selectionA['name'])
  descriptionA = (selectionA['description'])
  countryA = (selectionA['country'])
  follower_countA = (selectionA['follower_count'])
  print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}.")

  print(vs)

  random_numB = randint(1, 50)
  selectionB = data[random_numB]
  nameB = (selectionB['name'])
  descriptionB = (selectionB['description'])
  countryB = (selectionB['country'])
  follower_countB = (selectionB['follower_count'])

  print(F"Against B: {nameB}, a {descriptionB}, from {countryB}.")

  winner(follower_countA, follower_countB)
  print(winner(follower_countA, follower_countB))
  guess = input("Who has more followers? Type 'A' or 'B':").lower()
  while not game_end:
    if guess == winner(follower_countA, follower_countB):
      clear()
      score += 1
      print(logo)
      print(f"You're right! Current score: {score}.")
      selectionB = selectionA
      print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}.")

      print(vs)

      random_numB = randint(1, 50)
      selectionB = data[random_numB]
      nameB = (selectionB['name'])
      descriptionB = (selectionB['description'])
      countryB = (selectionB['country'])
      follower_countB = (selectionB['follower_count'])
      print(F"Against B: {nameB}, a {descriptionB}, from {countryB}.")

      winner(follower_countA, follower_countB)
      guess = input("Who has more followers? Type 'A' or 'B':").lower()
      continue
    else:
      clear()
      game_end = True
  print(logo)
  print(f"Sorry, that's wrong. Final score: {score}")

game()


