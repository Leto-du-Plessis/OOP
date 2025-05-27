import numpy as np
import numpy.random as rand

# config

# starting values
starting_food = [5, 10]
starting_wood = [0, 10]
starting_weapons = [0, 1]
starting_gold = [50, 101]

# eating parameters
min_eating_threshold = 50
max_eating_threshold = 80
cooked_food_increase = [45, 55]
uncooked_food_increase = [10, 20]
daily_hunger = [-15, -5]

# robbery
daily_robbery = 0.05
max_weapons_consumption = 10

# food gatherer
# --------------
# food
food_gatherer_minimum_food = 2
food_gatherer_comfortable_food = 3
food_gatherer_maximum_food = 6
# wood
food_gatherer_minimum_wood = 2
food_gatherer_comfortable_wood = 5
food_gatherer_maximum_wood = 8
# weapons
food_gatherer_minimum_weapons = 10
food_gatherer_comfortable_weapons = 15
food_gatherer_maximum_weapons = 20
# gathering
food_gatherer_maximum_food_gathered = 8
food_gatherer_minimum_food_gathered = 1
food_gatherer_maximum_wood_gathered = 2
food_gatherer_minimum_wood_gathered = 0
# selling
food_gatherer_minimum_food_price = 3
food_gatherer_minimum_wood_price = 5
food_gatherer_minimum_weapon_price = 10

# lumberjack
# --------------
# food
lumberjack_minimum_food = 4
lumberjack_comfortable_food = 5
lumberjack_maximum_food = 10
# wood
lumberjack_minimum_wood = 2
lumberjack_comfortable_wood = 4
lumberjack_maximum_wood = 6
# weapons
lumberjack_minimum_weapons = 10
lumberjack_comfortable_weapons = 15
lumberjack_maximum_weapons = 20
# gathering
lumberjack_maximum_food_gathered = 3
lumberjack_minimum_food_gathered = 0
lumberjack_maximum_wood_gathered = 10
lumberjack_minimum_wood_gathered = 5
# selling
lumberjack_minimum_food_price = 5
lumberjack_minimum_wood_price = 2
lumberjack_minimum_weapon_price = 10

# blacksmith
# --------------
# food
blacksmith_minimum_food = 6
blacksmith_comfortable_food = 8
blacksmith_maximum_food = 12
# wood
blacksmith_minimum_wood = 4
blacksmith_comfortable_wood = 6
blacksmith_maximum_wood = 10
# weapons
blacksmith_minimum_weapons = 2
blacksmith_comfortable_weapons = 4
blacksmith_maximum_weapons = 10
# crafting
blacksmith_weapons_crafted = 3
blacksmith_maximum_wood_gathered = 3
blacksmith_minimum_wood_gathered = 1 
# selling
blacksmith_minimum_food_price = 5
blacksmith_minimum_wood_price = 10
blacksmith_minimum_weapon_price = 6

personalities= ["conservative", "balanced", "liberal"]
conservative_base_money_desire = 50
balanced_base_money_desire = 100
liberal_base_money_desire = 150

class Worker: 

    hunger = 100

    def __init__(self):

        self.food = rand.randint(starting_food[0], starting_food[1]+1)
        self.wood = rand.randint(starting_wood[0], starting_wood[1]+1)
        self.weapons = rand.randint(starting_weapons[0], starting_weapons[1]+1)
        self.gold = rand.randint(starting_gold[0], starting_gold[1]+1)
        self.personality = personalities[rand.randint(0,3)]

    def eat(self):

        if self.hunger <= min_eating_threshold:
            while self.hunger <= max_eating_threshold:
                if self.food > 0:
                    if self.wood >= 2:
                        self.wood -= 1
                        self.food -= 1
                        self.change_hunger(rand.randint(cooked_food_increase[0], cooked_food_increase[1]+1))
                    else:
                        self.food -= 1
                        self.change_hunger(rand.randint(uncooked_food_increase[0], uncooked_food_increase[1]+1))
                else:
                    break

    def change_hunger(self, amount):

        self.hunger += amount
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100

    def daily_hunger(self):

        self.change_hunger(rand.randint(daily_hunger[0], daily_hunger[1]+1))

    def robbery(self):

        if rand.choice([True, False], p=[daily_robbery, 1-daily_robbery]): 
            defence_chance = min(self.weapons, 10)/10
            self.weapons = max(0, self.weapons-max_weapons_consumption)
            if rand.choice([True, False], p=[1-defence_chance, defence_chance]):
                self.food = self.food//2
                self.wood = self.wood//2
                self.weapons//2

    def personality_term(self):

        if self.personality == "conservative":
            return 2
        elif self.personality == "balanced":
            return 1
        else:
            return 0
        
    def money_desire(self):

        if self.personality == "conservative":
            desire = (conservative_base_money_desire - self.gold) // 35
            return max(0, min(8, desire+5))
        elif self.personality == "balanced":
            desire = (balanced_base_money_desire - self.gold) // 35
            return max(0, min(9, desire+5))
        else:
            desire = (liberal_base_money_desire - self.gold) // 35
            return max(0, min(10, desire+5))
        
    def breed(self):

        if self.hunger >= 98 and self.food >= 15:
            if rand.choice([True, False], p=[0.1, 0.9]):
                self.food - 10
                return True
        return False
        
class Food_Gatherer(Worker):

    def __init__(self):

        self.type = "food gatherer"
        super().__init__()

    def food_desire(self, weather: int = 50):

        if weather >= 80:
            weather_term = 2
        elif weather >= 50:
            weather_term = 1
        else:
            weather_term = 0
        
        if self.food <= food_gatherer_minimum_food:
            return 10
        elif self.food <= food_gatherer_comfortable_food:
            return min(10, 7 + weather_term + self.personality_term())
        elif self.food <= food_gatherer_maximum_food:
            return 5 + weather_term + self.personality_term()
        else:
            return 2 + weather_term + self.personality_term() * 2
        
    def wood_desire(self):

        if self.wood <= food_gatherer_minimum_wood:
            return 8 + self.personality_term()
        elif self.wood <= food_gatherer_comfortable_wood:
            return 4 + self.personality_term()
        elif self.wood <= food_gatherer_comfortable_wood:
            return 2 + self.personality_term()
        else:
            return 0 + self.personality_term() * 2
        
    def weapon_desire(self):

        if self.weapons <= food_gatherer_minimum_weapons:
            return 7 + self.personality_term()
        elif self.weapons <= food_gatherer_comfortable_weapons:
            return 5 + self.personality_term()
        elif self.weapons <= food_gatherer_maximum_weapons:
            return 3 + self.personality_term()
        else:
            return 1 + self.personality_term() * 2

    def gather(self, weather: int = 50):

        if self.food_desire() >= self.wood_desire():
            self.gather_food(weather)
        else:
            self.gather_wood()

    def gather_food(self, weather: int):
        self.food += max(0, rand.randint(food_gatherer_minimum_food_gathered, food_gatherer_maximum_food_gathered+1) - int(np.floor(rand.randint(0,5)/(weather/10))))
    
    def gather_wood(self):
        self.wood += rand.randint(food_gatherer_minimum_wood_gathered, food_gatherer_maximum_wood_gathered+1)

    def sell_food(self, food_price):
        if self.money_desire() >= self.food_desire() and self.food > food_gatherer_comfortable_food and food_price >= food_gatherer_minimum_food_price:
            food_for_sale = self.food - food_gatherer_comfortable_food 
            self.food -= food_for_sale
            return food_for_sale
    
    def sell_wood(self, wood_price):
        if self.money_desire() >= self.wood_desire() and self.wood > food_gatherer_comfortable_wood and wood_price >= food_gatherer_minimum_wood_price:
            wood_for_sale = self.wood - food_gatherer_comfortable_wood
            self.wood -= wood_for_sale
            return wood_for_sale
        
    def sell_weapons(self, weapon_price):
        if self.money_desire() >= self.weapon_desire() and self.weapons > food_gatherer_comfortable_weapons and weapon_price >= food_gatherer_minimum_weapon_price:
            weapons_for_sale = self.weapons - food_gatherer_comfortable_weapons
            self.weapons -= weapons_for_sale
            return weapons_for_sale
        
    def buy_food(self):
        if self.food_desire() > self.money_desire() and food_gatherer_maximum_food > self.food:
            desired_food = food_gatherer_maximum_food - self.food
            return desired_food
        
    def buy_wood(self):
        if self.wood_desire() > self.money_desire() and food_gatherer_maximum_wood > self.wood:
            desired_wood = food_gatherer_maximum_wood - self.wood
            return desired_wood
        
    def buy_weapons(self):
        if self.weapon_desire() > self.money_desire() and food_gatherer_maximum_weapons > self.weapons:
            desired_weapons = food_gatherer_maximum_weapons - self.weapons
            return desired_weapons

class Lumberjack(Worker): 

    def __init__(self):

        self.type = "lumberjack"
        super().__init__()

    def food_desire(self, weather: int = 50):

        if weather >= 80:
            weather_term = 2
        elif weather >= 50:
            weather_term = 1
        else:
            weather_term = 0
        
        if self.food <= lumberjack_minimum_food:
            return 10
        elif self.food <= lumberjack_comfortable_food:
            return min(10, 5 + weather_term + self.personality_term())
        elif self.food <= lumberjack_maximum_food:
            return 3 + weather_term + self.personality_term()
        else:
            return 0 + weather_term + self.personality_term() * 2
        
    def wood_desire(self):

        if self.wood <= lumberjack_minimum_wood:
            return min(10, 9 + self.personality_term())
        elif self.wood <= lumberjack_comfortable_wood:
            return 8 + self.personality_term()
        elif self.wood <= lumberjack_comfortable_wood:
            return 5 + self.personality_term()
        else:
            return 2 + self.personality_term() * 2
        
    def weapon_desire(self):

        if self.weapons <= lumberjack_minimum_weapons:
            return 8 + self.personality_term()
        elif self.weapons <= lumberjack_comfortable_weapons:
            return 5 + self.personality_term()
        elif self.weapons <= lumberjack_maximum_weapons:
            return 3 + self.personality_term()
        else:
            return 1 + self.personality_term() * 2

    def gather(self, weather: int = 50):

        if self.food_desire() >= self.wood_desire():
            self.gather_food(weather)
        else:
            self.gather_wood()

    def gather_food(self, weather: int):
        self.food += max(0, rand.randint(lumberjack_minimum_food_gathered, lumberjack_maximum_food_gathered+1) - int(np.floor(rand.randint(0,5)/(weather/10))))

    def gather_wood(self): 
        self.wood += rand.randint(food_gatherer_minimum_wood_gathered, food_gatherer_maximum_wood_gathered+1)

    def sell_food(self, food_price):
        if self.money_desire() >= self.food_desire() and self.food > lumberjack_comfortable_food and food_price >= lumberjack_minimum_food_price:
            food_for_sale = self.food - lumberjack_comfortable_food 
            self.food -= food_for_sale
            return food_for_sale
    
    def sell_wood(self, wood_price):
        if self.money_desire() >= self.wood_desire() and self.wood > lumberjack_comfortable_wood and wood_price >= lumberjack_minimum_wood_price:
                    wood_for_sale = self.wood - lumberjack_comfortable_wood
                    self.wood -= wood_for_sale
                    return wood_for_sale
        
    def sell_weapons(self, weapon_price):
        if self.money_desire() >= self.weapon_desire() and self.weapons > lumberjack_comfortable_weapons and weapon_price >= lumberjack_minimum_weapon_price:
            weapons_for_sale = self.weapons - lumberjack_comfortable_weapons
            self.weapons -= weapons_for_sale
            return weapons_for_sale
        
    def buy_food(self):
        if self.food_desire() > self.money_desire() and lumberjack_maximum_food > self.food:
            desired_food = lumberjack_maximum_food - self.food
            return desired_food
        
    def buy_wood(self):
        if self.wood_desire() > self.money_desire() and lumberjack_maximum_wood > self.wood:
            desired_wood = lumberjack_maximum_wood - self.wood
            return desired_wood
        
    def buy_weapons(self):
        if self.weapon_desire() > self.money_desire() and lumberjack_maximum_weapons > self.weapons:
            desired_weapons = lumberjack_maximum_weapons - self.weapons
            return desired_weapons

class Blacksmith(Worker):

    def __init__(self):

        self.type = "blacksmith"
        super().__init__()

    def food_desire(self, weather: int = 50):

        if weather >= 80:
            weather_term = 2
        elif weather >= 50:
            weather_term = 1
        else:
            weather_term = 0
        
        if self.food <= blacksmith_minimum_food:
            return 10
        elif self.food <= blacksmith_comfortable_food:
            return min(10, 7 + weather_term + self.personality_term())
        elif self.food <= blacksmith_maximum_food:
            return 6 + weather_term + self.personality_term()
        else:
            return 0 + weather_term + self.personality_term() * 2
        
    def wood_desire(self):

        if self.wood <= blacksmith_minimum_wood:
            return 9 
        elif self.wood <= blacksmith_comfortable_wood:
            return 5 + self.personality_term()
        elif self.wood <= blacksmith_comfortable_wood:
            return 3 + self.personality_term()
        else:
            return 1 + self.personality_term() * 2
        
    def weapon_desire(self):

        if self.weapons <= blacksmith_minimum_weapons:
            return 8
        elif self.weapons <= blacksmith_comfortable_weapons:
            return 5 + self.personality_term()
        elif self.weapons <= blacksmith_maximum_weapons:
            return 3 + self.personality_term()
        else:
            return 1 + self.personality_term() * 2

    def gather(self):

        if self.wood >= 2:
            self.wood -= 2
            self.weapons += blacksmith_weapons_crafted
        else:
            self.wood += rand.randint(blacksmith_minimum_wood_gathered, blacksmith_maximum_wood_gathered)

    def sell_food(self, food_price):
        if self.money_desire() >= self.food_desire() and self.food > blacksmith_comfortable_food and food_price >= blacksmith_minimum_food_price:
            food_for_sale = self.food - blacksmith_comfortable_food 
            self.food -= food_for_sale
            return food_for_sale
        
    def sell_wood(self, wood_price):
        if self.money_desire() >= self.wood_desire() and self.wood > blacksmith_comfortable_wood and wood_price >= blacksmith_minimum_wood_price:
            wood_for_sale = self.wood - blacksmith_comfortable_wood
            self.wood -= wood_for_sale
            return wood_for_sale
        
    def sell_weapons(self, weapon_price):
        if self.money_desire() >= self.weapon_desire() and self.weapons > blacksmith_comfortable_weapons and weapon_price >= blacksmith_minimum_weapon_price:
            weapons_for_sale = self.weapons - blacksmith_comfortable_weapons
            self.weapons -= weapons_for_sale
            return weapons_for_sale
        
    def buy_food(self):
        if self.food_desire() > self.money_desire() and blacksmith_maximum_food > self.food:
            desired_food = blacksmith_maximum_food - self.food
            return desired_food
        
    def buy_wood(self):
        if self.wood_desire() > self.money_desire() and blacksmith_maximum_wood > self.wood:
            desired_wood = blacksmith_maximum_wood - self.wood
            return desired_wood
        
    def buy_weapons(self):
        if self.weapon_desire() > self.money_desire() and blacksmith_maximum_weapons > self.weapons:
            desired_weapons = blacksmith_maximum_weapons - self.weapons
            return desired_weapons