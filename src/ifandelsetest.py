'''
DETAILS:
Still not working, I'm going to have to test around with changing
parentheses, 'and' statements, 'not' statements, 'or' statements, and
possibly look into how to do 'nor' statements.
'''

import os
from os import system, name

def clr():
    if name == 'nt':
        system('cls')
    
    else:
        system('clear')

def main():
    clr()
    print('Please type 6 boolean values below')
    print()
    print('Right:')
    slc2 = bool(input('2. (top-right) : '))
    slc3 = bool(input('3. (right)     : '))
    slc4 = bool(input('4. (bot-right) : '))
    print()
    print('Left:')
    slc6 = bool(input('6. (bot-left)  : '))
    slc7 = bool(input('7. (left)      : '))
    slc8 = bool(input('8. (top-left)  : '))
    print()
    print('Press \'ENTER\' to continue')

    #the top and bottom slices are not counted in any of these.        combo = when written together with a suffix.
    #top = 1 (combo 2, and 8)       bot/bottom = 5 (combo 4, and 6)      corner slices = 2, 4, 6, and 8       left = 7 (combo 6, and 8)      right = 3 (combo 2, and 4)

    #only one of the corner slices active
    if   (slc2) and not (slc3 and slc4 and slc6 and slc7 and slc8):
        middlepart = '  ・\'¨'

    elif (slc4) and not (slc2 and slc3 and slc6 and slc7 and slc8):
        middlepart = '  ・._'

    elif (slc6) and not (slc2 and slc3 and slc4 and slc7 and slc8):
        middlepart = '_.・  '

    elif (slc8) and not (slc2 and slc3 and slc4 and slc6 and slc7):
        middlepart = '¨\'・  '


    #only both corner slices or middle slices on either left or right
    elif (slc2 and slc4 or slc3) and not (slc6 and slc7 and slc8):
        middlepart = '  ・=:'

    elif (slc6 and slc8 or slc7) and not (slc2 and slc3 and slc4):
        middlepart = ':=・  '


    #only the top corner slice on the left and any other combinations on the right
    elif (slc2 and slc8) and not (slc3 and slc4 and slc6 and slc7):
        middlepart = '¨\'・\'¨'

    elif (slc2 and slc4 and slc8 or slc3 and slc8) and not (slc6 and slc7):
        middlepart = '¨\'・=:'

    elif (slc4 and slc8) and not (slc2 and slc3 and slc6 and slc7):
        middlepart = '¨\'・._'


    #only both corner slices or middle slices on either left and any other combinations on the right
    elif (slc2 and slc6 and slc8 or slc2 and slc7) and not (slc3 and slc4):
        middlepart = ':=・\'¨'

    elif (slc2 and slc4 and slc6 and slc8 or slc2 and slc4 and slc7 or slc3 and slc6 and slc8 or slc3 and slc6):
        middlepart = ':=・=:'

    elif (slc4 and slc6 and slc8 or slc4 and slc7) and not (slc2 and slc3):
        middlepart = ':=・._'


    #only the bot corner slice on the left and any other combinations on the right
    elif (slc2 and slc6) and not (slc3 and slc4 and slc7 and slc8):
        middlepart = '_.・\'¨'

    elif (slc2 and slc4 and slc6 or slc3 and slc6) and not (slc7 and slc8):
        middlepart = '_.・=:'

    elif (slc4 and slc6) and not (slc2 and slc3 and slc7 and slc8):
        middlepart = '_.・._'


    #no slices on the left nor the right
    elif not (slc2 and slc3 and slc4 and slc6 and slc7 and slc8):
        middlepart = '  ・  '
    
    #something went wrong
    else:
        middlepart = 'error'
    
    print()
    print('Middlepart = \'' + middlepart + '\'')
    print()
    print('Right:')
    print('Slice 2 (top-right) = \'' + str(slc2) + '\'')
    print('Slice 3 (right)     = \'' + str(slc3) + '\'')
    print('Slice 4 (bot-right) = \'' + str(slc4) + '\'')
    print()
    print('Left:')
    print('Slice 6 (bot-left)  = \'' + str(slc6) + '\'')
    print('Slice 7 (left)      = \'' + str(slc7) + '\'')
    print('Slice 8 (top-left)  = \'' + str(slc8) + '\'')
    print()
    input()
    main()
main()




'''
All middlepart variations:

#only one of the corner slices active
1.  '  ・\'¨'
2.  '  ・._'
3.  '_.・  '
4.  '¨\'・  '

#only both corner slices or middle slices on either left or right
5.  '  ・=:'
6.  ':=・  '

#only the top corner slice on the left and any other combinations on the right
7.  '¨\'・\'¨'
8.  '¨\'・=:'
9.  '¨\'・._'

#only both corner slices or middle slices on either left and any other combinations on the right
10. ':=・\'¨'
11. ':=・=:'
12. ':=・._'

#only the bot corner slice on the left and any other combinations on the right
13. '_.・\'¨'
14. '_.・=:'
15. '_.・._'

#no slices on the left nor the right
16. '  ・  '
'''