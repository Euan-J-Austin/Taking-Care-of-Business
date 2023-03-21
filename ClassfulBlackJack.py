#need a class to handle the flow of the game, and standard output
import os
import random


class Player:

  def __init__(self):
    self.cards1 = []
    self.cards2 = []  #in the case of Split
    self.cards1value = 0
    self.cards2value = 0
    self.purse = 100
    self.bet = 0


class DealerAsPlayer:

  def __init__(self):
    self.cards = []
    self.cardsvalue = 0
    self.bank = []


class DealerAsDealer:

  def __init__(self):
    self.presentdeck = [
      str(v) + s for v in range(1, 14) for s in ['C', 'S', 'D', 'H']
    ]

  def first_distribution(self):
    dap.cards = random.choices(self.presentdeck, k=1)
    for x in dap.cards:
      self.presentdeck.remove(x)
    player.cards1 = random.choices(self.presentdeck, k=2)
    for x in player.cards1:
      self.presentdeck.remove(x)
    eval.evaluate()

  def twist(self, x):
    if x == 'player':
      player.cards1.append(''.join(random.choices(self.presentdeck, k=1)))
      self.presentdeck.remove(player.cards1[-1])
      eval.evaluate()
    if x == 'dealer':
      dap.cards.append(''.join(random.choices(self.presentdeck, k=1)))
      self.presentdeck.remove(dap.cards[-1])


class Evaluator:

  def __init__(self):
    pass

  def evaluate(self):
    #need to fix this, loops over again only want to loop new additions after twist
    for v in player.cards1:
      if 1 < int(v[:-1]) < 11:
        player.cards1value += int(v[:-1])
      elif 10 < int(v[:-1]) <= 13:
        player.cards1value += 10
      elif int(v[:-1]) == 1:
        if player.cards1value + 11 <= 21:
          player.cards1value += 11
        elif player.cards1value > 21:
          player.cards1value += 1
    for v in dap.cards:
      if 1 < int(v[:-1]) < 11:
        dap.cardsvalue += int(v[:-1])
      elif 10 < int(v[:-1]) <= 13:
        dap.cardsvalue += 10
      elif int(v[:-1]) == 1:
        if dap.cardsvalue + 11 <= 21:
          dap.cardsvalue += 11
        elif dap.cardsvalue > 21:
          dap.cardsvalue += 1
    return eval.valuechecker()

  def valuechecker(self):
    display.general_output()
    if player.cards1value == 21:
      print('Blackjack, you win!')
    elif player.cards1value > 21:
      print('Bust!')
    elif player.cards1value < 21:
      x = input('Do you wish to stick or twist?')
      if x == 'S':
        pass
      if x == 'T':
        dad.twist('player')
      #Do you wish to hit or stick?


class BetHandler:

  def __init__(self):
    pass

  def placingbet(self):
    print(player.purse)
    print(player.bet)
    x = input('Place your bet: ')
    if int(x) > player.purse:
      print("Bet too large, insufficient funds.")
      return self.placingbet()
    if int(x) < player.purse:
      player.bet = int(x)
      player.purse = player.purse - player.bet
    return dad.first_distribution()


class PlayerDecisions:

  def __init__(self):
    pass


class Display:

  def __init__(self):
    pass

  def unicode_output(
      self, x):  #change to unicode formatting function, new standard output
    output_hand = []
    for s in x:
      #CLUBS
      if s == '1C':
        output_hand.append('A\u2663')
      elif s == '11C':
        output_hand.append('J\u2663')
      elif s == '12C':
        output_hand.append('Q\u2663')
      elif s == '13C':
        output_hand.append('K\u2663')
      elif s[-1] == 'C':
        output_hand.append(f'{s[:-1]}\u2663')
      #SPADES
      if s == '1S':
        output_hand.append('A\u2660')
      elif s == '11S':
        output_hand.append('J\u2660')
      elif s == '12S':
        output_hand.append('Q\u2660')
      elif s == '13S':
        output_hand.append('K\u2660')
      elif s[-1] == 'S':
        output_hand.append(f'{s[:-1]}\u2660')
      #DIAMONDS
      if s == '1D':
        output_hand.append('A\u2666')
      elif s == '11D':
        output_hand.append('J\u2666')
      elif s == '12D':
        output_hand.append('Q\u2666')
      elif s == '13D':
        output_hand.append('K\u2666')
      elif s[-1] == 'D':
        output_hand.append(f'{s[:-1]}\u2666')
      #HEARTS
      if s == '1H':
        output_hand.append('A\u2665')
      elif s == '11H':
        output_hand.append('J\u2665')
      elif s == '12H':
        output_hand.append('Q\u2665')
      elif s == '13H':
        output_hand.append('K\u2665')
      elif s[-1] == 'H':
        output_hand.append(f'{s[:-1]}\u2665')
    # if x == player.cards1:
    #   return print(
    #     f"Your hand is: {''.join(output_hand)}, valued at {player.cards1value}"
    #   )
    #   # if players_value > 21:
    #   #   print("YOUR BUST!")
    # else:
    #   return print(
    #     f"Dealer hand is: {''.join(output_hand)}, valued at {dap.cardsvalue}.")

    # #your cards and their value, dealer cards and their value, your bet, your purse
  def general_output(self):
    os.system('clear')
    print(f"""
    Your hand is {player.cards1}, valued at {player.cards1value}.
    Dealer hand is {dap.cards} valued at {dap.cardsvalue}.
    Your bet is {player.bet}$ and your purse has {player.purse}$.
    """)


dad = DealerAsDealer()
player = Player()
dap = DealerAsPlayer()
eval = Evaluator()
display = Display()
bet = BetHandler()
# dad.first_distribution()
bet.placingbet()