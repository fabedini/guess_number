#Random number
import random
random_number=random.randint(0,101)
guessestaken=True

while guessestaken:
  guess_number=input('Please enter your guess:')
  guess_number=int(guess_number)
  guessestaken +=1
  if guess_number < random_number:
    print('your guess is low,choose another one.')
  
  if guess_number > random_number:
    print('your guess number is high, choose another one.')
  
  if guess_number==random_number:
    print('your guess is unbelivabel')
    break




