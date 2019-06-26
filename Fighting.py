import random
import time

class Fighter:
    def __init__ (self, name, health, mindamage, maxdamage):
        self.name = name
        self.health = health
        self.mindamage = mindamage
        self.maxdamage = maxdamage   

    def start(self):        
        print(self.name, "has", self.health, "hp and deals", self.mindamage, "-", self.maxdamage, "damage")
        pass
        
def round(fighter1, fighter2):
    hit1 = random.randint(fighter1.mindamage, fighter2.maxdamage)
    hit2 = random.randint(fighter2.mindamage, fighter2.maxdamage)
    print(fighter1.name, "hits", fighter2.name, "for", hit1, "damage")
    print(fighter2.name, "hits", fighter1.name, "for", hit2, "damage")
    fighter1.health -= hit2
    fighter2.health -= hit1
    print("Now", fighter1.name, "has", fighter1.health, "hp, and", fighter2.name, "has", fighter2.health, "hp")
    print("----------------------")
    pass

def victory(fighter1, fighter2):
    if fighter1.health > 0:
        print(fighter2.name, "is dead,", fighter1.name, "has won!")
    elif fighter2.health > 0:
        print(fighter1.name, "is dead,", fighter2.name, "has won!")
    if fighter1.health <= 0 and fighter2.health <= 0:
        print("Both", fighter1.name, "and", fighter2.name, "are dead. It's a draw!")

def story(fighter1, fighter2):
    r = random.randint(0, 4)
    if r == 0:
        print(fighter1.name, "and", fighter2.name, "have met each other in the forest")
    elif r == 1:
        print(fighter1.name, "and", fighter2.name, "had a drunk conflict at the bar")
    elif r == 2:
        print(fighter1.name, "doesn't agree with philosophical position of", fighter2.name)
    elif r == 3:
        print("Both", fighter1.name, "and", fighter2.name, "want the same thing at the shop")
    elif r == 4:
        print("Nobody knows, why, but", fighter1.name, "and", fighter2.name, "start to fight!")  
        
def rumble(fighter1, fighter2):
    story(fighter1, fighter2)    
    fighter1.start()
    fighter2.start()
    print("----------------------")
    time.sleep(1)
    while fighter1.health > 0 and fighter2.health > -0:
        round(fighter1, fighter2)
        time.sleep(1)
    victory(fighter1, fighter2)


knight = Fighter("Knight", 20, 3, 5)
goblin = Fighter("Goblin", 20, 2, 6)
rumble(knight, goblin)

