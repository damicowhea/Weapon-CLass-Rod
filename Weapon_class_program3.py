import random

class Weapon:
    def __init__(self, name, description, power, value, call_sign):
        self.name = name
        self.description = description
        self.power = power
        self.value = value
        self.call_sign = call_sign
        # self.FULL = name + ': ' + description + '. ' + '\n  Power: ' + str(
        #     power) + '\n  Value: ' + str(
        #         value) + '\n To choose this item type: ' + call_sign + '\n'

    def get_full(self):
        """Generates and returns the full description of the weapon."""
        return self.name + ': ' + self.description + '. ' + '\n  Power: ' + str(
            self.power) + '\n  Value: ' + str(
                self.value) + '\n To choose this item type: ' + self.call_sign + '\n'

    def hit(self):
        """Returns the hit points for a use of the weapon."""
        return self.power * random.randint(1, 5)


sword = Weapon(name=' "Mighty Sword" ',
               description='a strong sword',
               power=10,
               value=25,
               call_sign='sword')
# print(sword.FULL)
print(sword.get_full())
dagger = Weapon(name=' "Sharp Dagger" ',
                description='a piercing dagger',
                power=8,
                value=15,
                call_sign='dagger')
#print(dagger.FULL)
print(dagger.get_full())
fart = Weapon(name=' "Fart of Despair" ',
              description='a fart like no other',
              power=1000,
              value=1000,
              call_sign='fart')
#print(fart.FULL)
print(fart.get_full())
pillow = Weapon(name=' "Short Pillow" ',
                description='a fluffy pillow',
                power=2,
                value=3,
                call_sign='pillow')
#print(pillow.FULL)
print(pillow.get_full())

while True:
    roll_value1 = (random.randint(1, 5))
    choice1 = input("Player 1, Which weapon would you like?")
    if choice1 == 'dagger':
        print('You chose' + dagger.name + '!')
        print(roll_value1 * dagger.power)
    elif choice1 == 'sword':
        print('You chose' + sword.name + '!')
        print(roll_value1 * sword.power)
    elif choice1 == 'fart':
        print('You chose' + fart.name + '!')
        print(roll_value1 * fart.power)
    elif choice1 == 'pillow':
        print('You chose' + pillow.name + '!')
        print(roll_value1 * pillow.power)
    else:
        print('Please type item as indicated on last line')
        continue
    break
#print("your roll was: " + str(roll_value1))
print('\n')

while True:
    roll_value2 = (random.randint(1, 5))
    choice2 = input("Player 2, Which weapon would you like?")
    if choice2 == 'dagger':
        print('You chose' + dagger.name + '!')
        print(roll_value2 * dagger.power)
    elif choice2 == 'sword':
        print('You chose' + sword.name + '!')
        print(roll_value2 * sword.power)
    elif choice2 == 'fart':
        print('You chose' + fart.name + '!')
        print(roll_value2 * fart.power)
    elif choice2 == 'pillow':
        print('You chose' + pillow.name + '!')
        print(roll_value2 * pillow.power)
    else:
        print('Please type item as indicated on last line')
        continue
    break
#print("your roll was: " + str(roll_value2))
print('\n')

if roll_value1 > roll_value2:
    print('Player 1 wins!')
elif roll_value1 < roll_value1:
    print('Player 2 wins!')
else:
    print(
        'It was a tie.  The odds of this happening are rare, so you become friends.'
    )
