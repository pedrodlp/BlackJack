############### Blackjack Project #####################
from art import logo
import random
import replit
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


def deal_card(hand):
    hand.append(random.choice(cards))


def calculate_score(hand):
    total = sum(hand)
    if len(hand) == 2 and total == 21:
        total = 0
    if total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total, hand

def compare(dealer, user):
  if dealer == 0 and user != 0:
    print("\nBlackJack! House wins.")
  elif user == 0  and dealer != 0:
    print("\nBlackJack! Player wins!")
  elif user > 21:
    print("\nYou went over 21. You Lose.")
  elif dealer > 21:
    print("\nDealer went over 21. You Win!")
  elif user > dealer:
    print("\nYou win!")
  elif dealer > user:
    print("\nHouse wins.")
  else:
    print("\nDRAW.")
  


game = True
while game:
  replit.clear()
  print(logo)
  flagG = True
  flagU = True
  user_cards = []
  computer_cards = []
  deal_card(computer_cards)
  deal_card(user_cards)
  deal_card(computer_cards)
  deal_card(user_cards)

  print(f"House first card: {computer_cards[0]}\n")
  totalc, computer_cards = calculate_score(computer_cards)

  print(f"Player's hand: {user_cards}\n")
  totalu, user_cards = calculate_score(user_cards)
  if totalu == 0:
    flagU = False
    flagG = False

#Player turn
  while flagU:
    if totalu < 22:
      if input("\nDo you want another card?: ") == "yes":
        deal_card(user_cards)
        totalu, user_cards = calculate_score(user_cards)
        print(f"\nPlayer's hand: {user_cards}")
      else:
        flagU = False
    else:
      flagU = False
      flagG = False

#Dealer turn
  print(f"\nHouse cards: {computer_cards}")
  while totalc < 17 and flagG and totalc != 0:
      print("\nHouse is taking another card.")
      deal_card(computer_cards)
      totalc, computer_cards = calculate_score(computer_cards)
      print(f"\nHouse cards: {computer_cards}")
  
  compare(totalc, totalu)
  if input("\nDo you want to play again? ") != "yes":
    game = False