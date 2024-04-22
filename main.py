############### Blackjack Project #####################
from replit import clear
from art import logo


import random
def deal_card():
  """"Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  dealt_card = random.choice(cards)
  return dealt_card
  
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "You draw"
  elif computer_score == 0:
    return "You lose, opponent has a blackjack"
  elif user_score == 0:
    return "You win with a blackjack"
  elif user_score > 21:
    return "You lose, you went over 21"
  elif computer_score > 21:
    return "You win, opponent went over 21"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      hit_or_pass = input("Type 'y' to deal another card, type 'n' to pass: ")
      if hit_or_pass == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
    
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
