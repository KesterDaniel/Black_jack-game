# blackjack capstone project
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_winner(player, computer):
  pass

def play():
  my_cards = []
  comp_cards = []

  for i in range(2):
    my_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))

  print(f"Your card: {my_cards}. Total = {sum(my_cards)}")
  print(f"Computer: {comp_cards[0]}")

  
  if sum(my_cards) == 21 and sum(comp_cards) == 21:
    print(my_cards)
    print(comp_cards)
    return print("DRAW")
  elif sum(my_cards) == 21:
    print(my_cards)
    print(comp_cards)
    return print("YOU WIN")
  elif sum(comp_cards) == 21:
    print(my_cards)
    print(comp_cards)
    return print("YOU LOSE")
  
  
  choice = input("Type d to draw or p to pass: ")
  player_end_game = False
  while player_end_game == False:
    if choice == "d":
      draw_card = random.choice(cards)
      if draw_card == 11 and draw_card + sum(my_cards) > 21:
        draw_card = 1
        my_cards.append(draw_card)
        print(my_cards)
      elif draw_card + sum(my_cards) > 21 and 11 in my_cards:
        my_cards[my_cards.index(11)] = 1
        my_cards.append(draw_card)
        print(my_cards)
      else:
        my_cards.append(draw_card)
        print(my_cards)

      if sum(my_cards) >= 21:
        player_end_game = True
        print(my_cards)
      else:
        choice = input("Type d to draw or p to pass: ")
    elif choice == "p":
      if sum(comp_cards) >= 17 :
        player_end_game = True
      else:
        draw_card = random.choice(cards)
        if draw_card == 11 and draw_card + sum(comp_cards) > 21:
          draw_card = 1
          comp_cards.append(draw_card)
        elif draw_card + sum(comp_cards) > 21 and 11 in comp_cards:
          comp_cards[comp_cards.index(11)] = 1
          comp_cards.append(draw_card)
        else:
          comp_cards.append(draw_card)
        
      
  print(my_cards)
  print(comp_cards)

      
        

        

play()

