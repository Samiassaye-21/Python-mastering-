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
""""
import random

Number = random.randint(1, 20)

def guess():
    print("I am thinking of a number between 1 and 20.")

guess()

for user in range(1, 7):
    Input = int(input("Enter your guess: "))

    if Number > Input:
        print("Your guess is too low.")
    elif Number < Input:
        print("Your guess is too high.")
    else:
        print("You won! You guessed it in " + str(user) + " attempts.")
        break

"""





##final project ##

##Number = int(input("Enter a number: "))##
""""
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    Number = int(input('Enter a number: '))
    
    while True:
        Number = collatz(Number)
        print(Number)
        if Number == 1:
            break

except:
    print('Enter only an integer number.')
"""

"""3. Simple ATM Simulator

Keep a balance variable. Write deposit(amount) and withdraw(amount)
 functions that use the global keyword to modify balance — but withdraw() 
 should refuse (print a message, don't crash) if amount > balance. Build a menu
   loop (while True) with options 1) Deposit, 2) Withdraw, 3) Check balance, 4)
Quit. Use try/except so entering letters instead of numbers doesn't crash
       the program,
 and continue to re-show the menu after invalid input instead of exiting."""

"""

import sys

balance = 12000
def deposit(amount):
    global balance
    balance = balance + amount
def withdraw(amount):
    global balance
    if amount > balance:
        print('You are not eligible')
    else:
        balance = balance - amount
while True:
    try:
        Menu = int(input(
            '1. Deposit  2. Withdraw  3. Balance  4. Quit: '
        ))
        if Menu == 1:
            Number = int(input('Enter the Amount: '))
            deposit(Number)

        elif Menu == 2:
            Number = int(input('Enter the Amount: '))
            withdraw(Number)
            print('your balance is ',balance)

        elif Menu == 3:
            print(balance)

        elif Menu == 4:
            sys.exit()

    except ValueError:
        print('You cannot use letters')

"""
     


"""

4. Temperature Converter Menu
Write celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f),
each just doing the math and returning a value (no printing inside them — 
this practices separating calculation from display, a big function-design lesson). 
Build a for loop menu using range() is not needed here — instead use while True with 
if/elif/else to route to the right function based on user choice, 
try/except for bad number input, and let the user type 'exit' to stop.
"""
"""
def celsius (number):
   num = 9 * number
   return num
def fahrenheit(number):
   num = 5 * number
   return num 

while True:
    try :

        user=(int (input('enter a number if you want celsius to farniet choose 1 other wise 2 ')))
        if user==1:
            user= int(input('enter the amount'))
            print(celsius(user))
        elif user==2:
            user = int(input('enter the amount'))
            fahrenheit(user)
        else:
            print ('you have error')

    except ValueError:
        print('it undefined')
"""

"""
Times Table Quiz (uses for + range() + functions + scope)
Write ask_question(a, b) that prints f"What is {a} x {b}?", 
takes the answer via input(), and returns True/False for whether it's correct. In your main program
, use a for loop with range() to generate say 5 random multiplication questions (import random, pick two
 numbers 1-12 each loop), call ask_question() each time, use try/except in case they type non-numbers, 
 and keep a running score — increment it with the global statement inside a helper function
   record_result(correct). Print the final score out of 5 at the end.
"""
