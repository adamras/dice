import random

dice_sides = raw_input("How many sides to the dice? 4, 6, 8, 10 or 20 ")
number = random.randint(1,(int (dice_sides)))
print ("Your die roll is:" + str(number))