##A major purpose of functions is to group code that gets executed multiple times##
#import random#
"""def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it s certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
r = random.randint(0,9)
print(getAnswer(r))
## single equivalent line ##
print (getAnswer(random.randint(0,9))) """

## execption handling ##
"""def spam (num ):
    try:
        return 42/ num
    except ZeroDivisionError:
        print ('error invalid number ')

print(spam(5))
print (spam(0))
"""



"""
import random
def guess():
    num = random.randint(1,20)
    return num
def yourNumber():
  person = int(input('what is your number guessed.  ?'))
  return person
    

number = guess()
hey = yourNumber()

if number>hey:
    print('your number is less than we expect ')
elif number<hey:
   print('your number is greater than we expect ')
elif number==hey:
   print ('you won the game ')
   
print(guess())
print(yourNumber())

"""


import random
guess = random.randint(1,20)
## Asking the user number ##
def userInput():
    Ask = int(input('Enter your guess number '))
    return Ask
for user in range (1,6):
    person =userInput
if guess>person:
        print('your guess it too low ')
        userInput()
elif guess <person:
 print('your guess is greater ')
elif guess == person:
    print('YOU WON THE GAME')





 





