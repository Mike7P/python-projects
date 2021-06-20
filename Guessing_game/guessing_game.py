
print("Welcome to Kelly's Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts = 0
difficulty_choosing = False
random_num = randint(1, 100)
# print(f"Pssst, the correct answer is {random_num}")

def guessing_func(guess, random_num):
  global attempts
  attempts -= 1
  if guess == random_num or attempts == 0:
    return 0
  elif guess < random_num:
    print('Too low!')
  elif guess > random_num:
    print('Too high!')

while not difficulty_choosing:
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if choice == 'easy':
    attempts = 10
    difficulty_choosing = True
  elif choice == 'hard':
    attempts = 5
    difficulty_choosing = True
  else: 
    print("Sorry, I have no idea what you typed but it wasn't easy or hard!!")
game_go = True
while game_go:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  guess_good = guessing_func(guess, random_num)
  if guess_good == 0:
    game_go = False

if guess == random_num:
  print(f"You got it! The answer was {guess}.")
else:
  print(f"Game over! {attempts} attempts left!! ")
