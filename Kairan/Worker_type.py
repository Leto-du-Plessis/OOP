from OOP.Kairan.Worker_classes import Worker
import numpy as np



class Farmer(Worker):


    
    def grow_food(self):
        self.food = self.food + np.random.randint(0,11)

    def find_wood(self):
        self.wood = self.wood + np.random.randint(0,3)

    def action(self):
        if self.food > 15 and self.gold <5:
            Farmer.find_wood(self)
        else:
            Farmer.grow_food(self)



class Lumberjack(Worker):

    def cut_wood(self):
        self.wood = self.wood + np.random.randint(0,6)

    def subsistence_farming(self):
        self.food = self.food + np.random.randint(0,4)
    
    def action(self):
        if self.wood>15 and self.gold < 5:
            Lumberjack.subsistence_farming(self)
        else:
            Lumberjack.cut_wood(self)

class Blacksmith (Worker):

    def smith(self):
        self.weapons = self.weapons + 1
            
    def action(self):
        if self.wood >=2:
            Blacksmith.smith(self)
            self.wood = self.wood -2




