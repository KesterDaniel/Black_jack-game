# blackjack capstone project
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_card(new_card, prev_stack):
  """Add a new card to the previous stack"""
  if new_card == 11 and new_card + sum(prev_stack) > 21:
    new_card = 1
    prev_stack.append(new_card)
  elif new_card + sum(prev_stack) > 21 and 11 in prev_stack:
    prev_stack[prev_stack.index(11)] = 1
    prev_stack.append(new_card)
  else:
    prev_stack.append(new_card)

def play():
  wannaplay = input("Do you wanna play a game of blackjack? Type y for yes or n for no: ")
  if wannaplay == "y":
    player_cards = []
    comp_cards = []

    for i in range(2):
      player_cards.append(random.choice(cards))
      comp_cards.append(random.choice(cards))

    print(f"Your cards: {player_cards}. Total = {sum(player_cards)}")
    print(f"Computer first card: {comp_cards[0]}")

    
    if sum(player_cards) == 21 and sum(comp_cards) == 21:
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      return print("DRAW")
    elif sum(player_cards) == 21:
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      return print("BLACKJACK")
    elif sum(comp_cards) == 21:
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      return print("Computer BLACKJACK. YOU LOST")
    
    
    choice = input("Type d to draw or p to pass: ")
    player_end_game = False
    while player_end_game == False:
      if choice == "d":
        draw_card = random.choice(cards)
        add_card(draw_card, player_cards)
        print(f"Your cards: {player_cards}, Total = {sum(player_cards)}")

        if sum(player_cards) >= 21:
          player_end_game = True
        else:
          choice = input("Type d to draw or p to pass: ")
      elif choice == "p":
        if sum(comp_cards) > 17 :
          player_end_game = True
        else:
          draw_card = random.choice(cards)
          add_card(draw_card, comp_cards)
          
    if sum(player_cards) > 21:
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      print("You went over. You LOST, Computer WON")
    elif sum(comp_cards) > 21:
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      print("Computer went over. You WON, Computer LOST")
    elif sum(comp_cards) == sum(player_cards):
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      print("DRAW")
    elif sum(player_cards) == 21:
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      print("BLACKJACK")
    elif sum(comp_cards) == 21:
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      print("Computer BLACKJACK. YOU LOST")
    elif sum(comp_cards) > sum(player_cards):
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      print("You LOST, Computer WON")
    elif sum(player_cards) > sum(comp_cards):
      print(f"Your cards: {player_cards}, Total: {sum(player_cards)}")
      print(f"Computer cards: {comp_cards}, Total: {sum(comp_cards)}")
      print("You WON, Computer LOST")
  
    play()

play()

