from art import logo
import random
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_a_card(deck):
  deck.append(random.choice(cards))
  return deck

def deal():
  two_cards = []
  for num in (0,2):
    two_cards.append(random.choice(cards))
  return two_cards

def total(player_deckR, computer_deckR, dict):
  totalp = 0
  totalc = 0
  for num in computer_deckR:
    totalc += num
  for num in player_deckR:
    totalp += num
  dict['You'] = totalp
  dict['Computer'] = totalc
  return players_dict

def winner(players_dictR):
  for key in players_dictR:
          score = players_dictR[key]
          winner = 0
          if score > winner:
           winner = key
  return winner


start = input("Hi, would you like to play Blackjack? Type 'y' or 'n:' ")
if start == 'y':
  game_continue = True
else: 
  game_continue = False
  question = input("Do you want to play again? 'y' or 'n:' ")

players_dict = {}
player_cards = deal()
computer_cards = deal()

print(f"Your starting deal: {player_cards}")
print(f"Computers starting deal: {computer_cards[0]}'?'")
score_dict = total(player_cards, computer_cards, players_dict)
choice = input("If you would like to stick type 'S' or for another card type 'h' for hit: ")
if choice == 's':
  while sum(computer_cards) < 17:
    deal_a_card(computer_cards)
  if sum(computer_cards) > 21:
    print(total(player_cards, computer_cards, players_dict))
    print('Computer went BUST! You win!!')
  else:
    print(total(player_cards, computer_cards, players_dict))
    print(f"The winner is the {winner(players_dict)}!!")



# print(total(player_cards, computer_cards, players_dict))
# print(player_cards)
print(computer_cards)
# print(winner(players_dict))
