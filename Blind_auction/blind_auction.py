def add_to_dict(name, bid,):
  auction_dict[name] = bid
  
auction_finished = 0
auction_dict = {}

while auction_finished == False:
    print("Welcome to the secret auction program\n")
    name_input = input('What is your name? ').lower()
    bid_input = input('What is your bid? $')
    decision_input = input('Are there any other bidders? Type "yes" or "no" ').lower()
    bid_input = int(bid_input)
    
    add_to_dict(name_input, bid_input)
    print(auction_dict)
    if decision_input == 'yes':
      clear()
      continue
    else:
        clear()
        auction_finished == False
        
        for key in auction_dict:
          score = auction_dict[key]
          winner = 0
          if score > winner:
           winner = key
    print(f'The winner is {winner} with a bid of ${auction_dict[winner]}')
