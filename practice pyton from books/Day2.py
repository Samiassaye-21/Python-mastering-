""" while loop concept 
name = 'CHA'
print ('what is your name ')
Name = input ()
while name==Name:
   print ('thank you ')
   break 
if name !=Name:
   print ('please try again ')
   Name = input()
   
for i in range(5):
    print (i)
    



for i in range (16,10,-2):
    print (i)

    """


## importing from modules like random , math, sys, ##
"""import sys 

while True:
    print ('what is your name ?')
    response = input()
    if response == 'exit':
         print ('thank you for all the services ' + response )
         sys.exit()
       
"""


import math 
import sys

name = input ('what is your name ')
age = input ('Enter your age ')
age = int (age )
if age>10:
    for age in range (1,10,3):
       print (age)
elif age<10:
    while True:
        print (math.sqrt(age))
        choice = input ('do you want to try again ?')
        if choice == 'yes ':
          age = int(input('Enter your age' ))
        elif choice != 'yes':
            print ('thank you ' + name )
            break
##"""##
