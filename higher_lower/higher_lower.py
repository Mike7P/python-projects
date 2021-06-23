#  Higher or Lower
from art import logo
from art import vs
from game_data import data
from random import randint
from replit import clear

def winner(a, b):
  if a > b:
    return 'a'
  else: return 'b'



# Print logo = Higher / Lower
print(logo)
# Create ---
# selection A vairable
# selection B vairable
selectionA = []
selectionB = []
score = 0
game_end = False
# Generate a random dictionary selection and label A

# How many entries are there?
# 50
# Generate a random number between 1 and that...
# def generate_selection(data):
#   selection = []
#   random_num = randint(1, 50)
#   selection = data[random_num]
#   return selection

random_numA = randint(1, 50)
selectionA = data[random_numA]
# name = (selectionA['name'])
# description = (selectionA['description'])
# country = (selectionA['country'])

nameA = (selectionA['name'])
descriptionA = (selectionA['description'])
countryA = (selectionA['country'])
follower_countA = (selectionA['follower_count'])
print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}.")

# Print VS Symbol
print(vs)


# # Generate a random dictionary selection and label B
# ----
# Generate a random number between 1 and that...
random_numB = randint(1, 50)
selectionB = data[random_numB]
nameB = (selectionB['name'])
descriptionB = (selectionB['description'])
countryB = (selectionB['country'])
follower_countB = (selectionB['follower_count'])
# print(follower_countA)
# print(follower_countB)

print(F"Against B: {nameB}, a {descriptionB}, from {countryB}.")

# Take input and compare win or lose
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
    # print(winner(follower_countA, follower_countB))
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    continue
  else:
    clear()
    game_end = True
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
# Create score for right answers
# 
#  if win
# print(f"You're right! Current score: {1}.")
# Generate a random dictionary selection and label B
# selection B becomes selection A

# if lose
# print(f"Sorry, that's wrong. Final score: {score}")
