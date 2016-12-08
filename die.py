import random

print("Greetings Champion.  Cast your die.  Witness your destiny.")
print("")
times = raw_input("How many die to roll? ")
sides = raw_input("How many sides on the dice? ")

print("Rolling " + times + "D" + sides)
print("")


class Die(object):
    def roll(self):
        return random.randint(1, (int(sides)))

d = Die()
rolls = []

for time in range(int(times)):
    y = d.roll()
    print ("This is your roll:%s" % y)
    rolls.append(y)

total = 0
for x in rolls:
    total = total + x

print("")
print ("You have rolled a total of %s" % total)

print("")
print ("Slay that dragon, hero!")


