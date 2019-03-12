#This is a basic version of Blackjack that I created to improve my knowledge of Python
#Possible ways to improve this: Adding Card Counting, Making Ace Change Values Depending on the Situation, add a money system and betting
#Long term way to improve would be to add a GUI, a Computer that uses a strategy, and to add the complete rules

import random as rand
import time

#Self-Created Functions
def check():
  if(computerSum >= 22):
    exit()

def stand():
  exit()

def hit():
  exit()

def display(player):
  if(player == "person"):
    print "Your Cards: " + str(playerSum)
    for cardNumber, cardValue in enumerate(playerCards, 1):
      print("Card %s: %s" % (cardNumber, cardValue))
    print ""
  
  else:
    print "Computer's Cards: " + str(computerSum)
    for cardNumber, cardValue in enumerate(computerCards, 1):
      print("Card %s: %s" % (cardNumber, "?"))
    print ""
    
def deal():
  print "Dealing..."
  time.sleep(1)
  print "Here are the cards!"
  print ""
  display("person")
  display("computer")
    
  drawAnswer = raw_input("Do you stand or hit?")
  if drawAnswer == "stand":
    stand()
  elif drawAnswer == "hit":
    hit()



#New Game Variables
playerSum = 0
computerSum = 0

playerCards = [rand.randint(1,11), rand.randint(1,10)]
playerSum = sum(playerCards)

computerCards = [rand.randint(1,11), rand.randint(1,10)]
computerSum = sum(computerCards)

#Game Beigns
gameOngoing = True
while gameOngoing:
  print "Welcome to Blackjack!"
  print ""
  deal()
  

    
#Notes: Give how many times won at the end, change all "player"'s' to "person"'s,' generalize display() function, create secretDisplay() funtion