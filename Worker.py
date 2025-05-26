import numpy as np
import numpy.random as rand

personalities= ["conservative", "balanced", "liberal"]

class Worker: 

    hunger = 100

    def __init__(self):

        self.food = rand.randint(5, 11)
        self.wood = rand.randint(0, 11)
        self.weapons = rand.randint(0, 11)
        self.gold = rand.randint(100, 1001)
        self.personality = personalities[rand.randint(0,3)]

    def eat(self):

        if self.hunger <= 50:
            while self.hunger <= 80:
                if self.food > 0:
                    if self.wood >= 2:
                        self.wood -= 1
                        self.food -= 1
                        self.change_hunger(rand.randint(45, 56))
                    else:
                        self.food -= 1
                        self.change_hunger(rand.randint(10, 21))
                else:
                    break

    def change_hunger(self, amount):

        self.hunger += amount
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100

    def robbery(self):

        if rand.choice([True, False], p=[0.05, 0.95]): 
            defence_chance = min(self.weapons, 10)/10
            self.weapons = max(0, self.weapons-10)
            if rand.choice([True, False], p=[1-defence_chance, defence_chance]):
                self.food = self.food//2
                self.wood = self.wood//2
                self.weapons//2
            
    
