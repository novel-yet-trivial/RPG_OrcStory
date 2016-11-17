#!/usr/bin/env python3

"""
A description of your program goes here.
"""

import time
import random

class Character:
    """
    A description of this class goes here.
    """
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def fight(self, other):
        while other.health > 0:
            swings = random.randint(1,10)
            if swings <=2:
                print("you missed, he punched you in the face")
                self.health -= 10
                other.health += 1
            elif swings <= 3:
                print("you hit the {} for 3".format(other.name))
                other.health -= 3
            elif swings <=6:
                print("you hit the {} for 6".format(other.name))
                other.health -= 6
            elif swings <= 10:
                print("CRIT")
                other.health -= 9
            time.sleep(2)

        print("you slain the {}".format(other.name))


def main():
    user_name = input("You are new here, What's your name?")

    fighter = Character(user_name, 20, 10, 14) #make an instance of the class to use
    orc = Character("Orc", 20, 12, 8)
    wolf = Character("Wolf", 10, 5, 3)

    silver_bag = 0

    starts=("Ah, {}. That's a good name, I'm Ahab, OH SHIT THATSAORC IMOUT \n\n".format(user_name))
    print(starts)
    time.sleep(2)
    fighter.fight(orc)
    print("\n")
    print("Damn, good job taking care of that Orc, here's five silver")
    time.sleep(1)
    silver_bag += 5
    print("\n")
    print("Oh no! Here's the wolf!")
    fighter.fight(wolf) #see how easily we can reuse a method if it's written correctly
    print("Damn, good job taking care of that Wolf, here's another five silver")
    silver_bag += 5

if __name__ == '__main__':
    main()
