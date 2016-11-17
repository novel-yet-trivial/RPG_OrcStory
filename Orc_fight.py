import time
import random

class Fighter: #Hero's stats
    Health = 20
    Attack = 10
    Defense = 14

class Orc : #Enemy Orc Stats
    Health = 30
    Attack = 12
    Defense = 8

class Wolf: #Enemy Wolf Stats
    Health = 10
    Attack = 5
    Defense = 3

Silver_Bag = 0

if Silver_Bag < 2:
    print("You now have " + str(Silver_Bag) + " piece of silver!")
else:
    print("You now have" + str(Silver_Bag) + "pieces of silver")


def Orc_fight(): # What happens when you encounter an Orc
	while Orc.Health >0:
		swings = random.randint(1,10)
		if swings <=2:
			print("you missed, he punched you in the face")
			Fighter.Health = Fighter.Health - 10
			Orc.Health = Orc.Health + 1
			time.sleep(2)
		if swings <= 3:
			print("you hit the Orc for 3")
			Orc.Health = Orc.Health - 3
			time.sleep(2)
		if swings <=6:
			print("you hit the Orc for 6")	
			Orc.Health = Orc.Health - 6
			time.sleep(2)
		if swings <= 10:
			print("CRIT")
			Orc.health = Orc.Health - 9
			time.sleep(2)
		if Orc.Health <=0:
			print("you slain the Orc")
			break
Introduction = input("You are new here, What's your name?")
Starts=("Ah, " + Introduction + " That's a good name, I'm Ahab, OH SHIT THATSAORC IMOUT \n\n")
print(Starts)
time.sleep(2)
Orc_fight()
print("\n")
print("Damn, good job taking care of that Orc, here's five silver")
time.sleep(1)
Silver_Bag +=1
print("\n")







        

        

        
    
