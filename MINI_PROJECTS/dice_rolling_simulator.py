# You rolled: 4
# Roll again? (yes/no): yes
# You rolled: 6
# Roll again? (yes/no): no
# Thanks for playing!

import random

while True: # We have used while True because we don't know how many times the user wants to roll the dice. They might roll twice, five times, or twenty times.
    dice = random.randint(1,6)
    print(f"You rolled : {dice}")
    choice = input("Roll again? (yes/no) :")
    if(choice.lower() == 'no'):
        print(f"Thanks for playing!")
        break


