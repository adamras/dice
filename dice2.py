import random
import sys

dice_sides = sys.argv[1]
number = random.randint(1,(int (dice_sides)))
print ("Your die roll is:" + str(number))
