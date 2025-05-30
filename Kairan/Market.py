from Worker_classes import *
from Worker_type import *
import numpy as np

class Market:
    def __init__(self, wood_stock, food_stock, weapon_stock):
        self.wood_stock = wood_stock
        self.food_stock = food_stock
        self.weapon_stock = weapon_stock

    array = [[[]for i in range(2)] for i in range (3)]

    def sale(self, worker):
        if worker.weapons > 10:
            x = worker.weapons - 10
            worker.weapons -= x
            self.array[2][0].append(x)
    def price_weapons(self):
        count = len(self.array[2])
        if count > 100:
            price = 1

        elif  75 < count <= 100:
            price = 2

        elif 50 < count <= 75:
            price = 3
        
        elif 25 < count <= 50:
            price = 4

        else:
            price = 5 

        self.array[2][1] .append(price)  

    def market(self, worker):
        Market.sale(self, worker)
        Market.price_weapons(self)
        print(self.array)



man1 = Blacksmith(2, 10, 10, 15)

market = Market(10, 10, 10)



x=0
while x != 100 or man1.alive() == False:
    man1.action()
    
    if man1.alive() == True:
        man1.hunger()
        man1.eat()
        market.market(man1)
    else:
        break    
    print(f'wood total', man1.wood)
    print(f'food total', man1.food)
    print(f'weapon total',man1.weapons)
    print(f'day',x, 'over')
    x = x + 1