#Random game:can you gues the right number
print('hello, my name is Fatemeh.\nDo you Want to play with me?')
user_answer=input()
answer='yes'

if user_answer== answer:
  user_name=input('What is your name:\n')
  print('Okay.',user_name,'lets do it.')
else:
  print('Whatever you want.Bye!')
  exit()

import random
random_number=random.randint(0,101)
Game_state=True # how many times user can guess the number

while Game_state: #do the statement until Game_state is True
  guess_number=int(input('Please enter your guess:'))
  
  if guess_number < random_number:
    print('your guess is low,choose another one.')
    continue
  
  if guess_number > random_number:
    print('your guess number is high, choose another one.')
    continue
  
  if guess_number==random_number:
    print('your guess is unbelivabel')
    break # or:Game_state=False





