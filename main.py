import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
print(computer)

player = input("Choose rock, paper, or scissors: \n")

print("player choice is: " + player)

# Who wins
if player == computer:
  print("U GUYS BOTH TIED NO WAY BRUV")
else:
  if player == "rock":
    if computer == "paper":
      print("computer WON BRUV")
    else:
      print("player WON BRUV")
  elif player == "paper":
    if computer =="scissors":
      print("computer WON MAN")
    else:
      print("player won bruv")
  else:
    if computer == "rock":
      
      print("Computer won!")
    else:
      print("player won!")




