# Snake / Water / Gun or Rock / Paper / Scissors

import random
from re import S
def gameWin(comp, you):
  if comp==you:
    return None
  elif comp=='s':
    if you=='w':
      return False
    elif you=='g':
      return True
  elif comp=='w':
    if you=='g':
      return False
    elif you=='s':
      return True
  else:
    if you=='s':
      return False
    elif you=='w':
      return True
print("comp turn: Snake(s) or Water(w) or Gun(g)? --- ")
randNo = random.randint(1,3)
if randNo==1:
  comp='s'
elif randNo==2:
  comp= 'w'
elif randNo==3:
  comp= 'g'
you = input("your turn: Snake(s) or Water(w) or Gun(g)? = ")

print(f"computer chose =  {comp}")
print(f"You chose = {you}")
a = gameWin(comp, you)
if a==None:
  print("the game is tie!")
elif a:
  print("You Win!")
else:
  print("You Lose!")