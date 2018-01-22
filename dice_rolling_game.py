import random
def dice_roll():
    y=random.randint(1,6)
    print(y)
    input_value()

def input_value():
    i=input('Would you like to roll? Please enter Yes or No:')
    compare_value(i)
    
def compare_value(i):
    if i == 'Yes':
        dice_roll()
    elif i == 'No':
        print('Welcome again')
    else:
        i=input('Please input valid value:')
        compare_value(i)

dice_roll()

