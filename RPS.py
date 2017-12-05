"""
The program should do the following:

1. Prompt the user to select either Rock, Paper, or Scissors.
2. Instruct the computer to randomly select either Rock, Paper, or Scissors.
3. Compare the user's choice and the computer's choice.
4. Determine a winner (the user or the computer).
5. Inform the user who the winner is.

"""
from random import randint
from time import sleep

options = ["R", "P", "S"]

LOSS_MESSAGE = "You lost!"

WON_MESSAGE = "You won!"

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Computer selected: %s" % computer_choice
  
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
    
  elif user_choice_index == 0 and computer_choice_index == 2:
    print WON_MESSAGE
    
  elif user_choice_index == 1 and computer_choice_index == 0:
    print WON_MESSAGE
    
  elif user_choice_index == 2 and computer_choice_index == 0:
    print WON_MESSAGE
    
  elif user_choice_index > 2:
    return
  
  else:
    print LOSS_MESSAGE
    
def play_RPS():
  print "Rock, Paper, or Scissors?"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice = options[randint(0, len(options) - 1)]
  
  decide_winner(user_choice, computer_choice)
  
play_RPS()
