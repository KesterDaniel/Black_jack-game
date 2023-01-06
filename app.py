# blackjack capstone project
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play():
  my_cards = []
  comp_cards = []

  for i in range(2):
    my_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))

  print(my_cards)
  print(comp_cards)

play()
