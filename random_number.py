#Random number
import random
random_number=random.randint(0,101)
Game_state=True

while Game_state:
  guess_number=int(input('Please enter your guess:'))
  
  if guess_number < random_number:
    print('your guess is low,choose another one.')
    continue
  
  if guess_number > random_number:
    print('your guess number is high, choose another one.')
    continue
  
  if guess_number==random_number:
    print('your guess is unbelivabel')
    break





