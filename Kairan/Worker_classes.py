import numpy as np

class Worker:
    hunger_level = 100
    maximum = 80
    minimum = 30
    def __init__(self, food, wood, gold, weapons):
        self.food = food
        self.wood = wood
        self.gold = gold
        self.weapons = weapons

    def hunger(self):
        self.hunger_level = self.hunger_level - np.random.randint(20,31)
        print(f'The hunger before eating', self.hunger_level)

    def eat(self):
        will=np.random.randint(0,10)
        print(f'The will to eat', will)
        if self.hunger_level <= self.minimum and self.food > 0:
            if self.food > 0 and self.wood > 0:
                self.food = self.food -1
                self.wood = self.wood -1
                self.hunger_level = self.hunger_level + np.random.randint(45,55)                    
            else:
                self.food = self.food-1
                self.hunger_level = self.hunger_level + np.random.randint(10,21)

        if will >= 3:

            if self.minimum < self.hunger_level < self.maximum:
                if self.food >=0:
                    if self.wood >=2 and self.hunger_level < 50:
                        self.wood = self.wood - 1
                        self.food = self.food - 1
                        self.hunger_level = self.hunger_level + np.random.randint(45,55)
                
                    elif self.hunger_level > 50:
                        self.food = self.food - 1
                        self.hunger_level = self.hunger_level + np.random.randint(10,21)
                
                
                    else:
                        self.food = self.food-1
                        self.hunger_level = self.hunger_level + np.random.randint(10,21)



        print(f'the hunger level after eating:', self.hunger_level)

    def alive(self):
        alive = True


        if self.hunger_level <= 0:
            alive = False  
        return alive



