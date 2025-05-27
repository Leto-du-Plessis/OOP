import numpy as np
import numpy.random as rand
import typing 

# config
base_food_price = 10
min_food_price = 1
max_food_price = 100
base_food_amount = 20
base_wood_price = 15
min_wood_price = 1
max_wood_price = 150
base_wood_amount = 20
base_weapon_price = 20
min_weapon_price = 5
max_weapon_price = 500
base_weapon_amount = 10

class ResourceMarket:

    def __init__(self, base_price: int, min_price: int, max_price: int, base_amount: int):

        self.listings = {}
        self.base_price = base_price
        self.min_price = min_price
        self.max_price = max_price
        self.base_amount = base_amount
    
    def get_amount(self):
        return sum(self.listings.values())
    
    def get_price(self, amount):
        return max(self.min_price, min(self.max_price, self.base_price - int((amount - self.base_amount))))
    
    def set_listing(self, listing: dict):
        self.listings.update(listing)

    def get_listing_of(self, worker_id):
        if worker_id in self.listings.keys():
            return self.listings[worker_id]
        return None
    
    def purchase(self):
        id = rand.choice(list(self.listings.keys()))
        self.listings[id] -= 1
        if self.listings[id] <= 0:
            self.listings.pop(id)
        return int(id)
    
class Market:

    def __init__(self):

        self.food_market = ResourceMarket(base_food_price, min_food_price, max_food_price, base_food_amount)
        self.wood_market = ResourceMarket(base_wood_price, min_wood_price, max_wood_price, base_wood_amount)
        self.weapon_market = ResourceMarket(base_weapon_price, min_weapon_price, max_weapon_price, base_weapon_amount)

    def get_food_amount(self):
        return self.food_market.get_amount()
    
    def get_wood_amount(self):
        return self.wood_market.get_amount()
    
    def get_weapon_amount(self):
        return self.weapon_market.get_amount()
    
    def get_food_price(self):
        return self.food_market.get_price(self.get_food_amount())
    
    def get_wood_price(self):
        return self.wood_market.get_price(self.get_wood_amount())
    
    def get_weapon_price(self):
        return self.weapon_market.get_price(self.get_weapon_amount())
    
    def set_food_listing(self, listing: dict):
        self.food_market.set_listing(listing)
    
    def set_wood_listing(self, listing: dict):
        self.wood_market.set_listing(listing)

    def set_weapon_listing(self, listing: dict):
        self.weapon_market.set_listing(listing)

    def get_food_listing_of(self, worker_id):
        return self.food_market.get_listing_of(worker_id)
    
    def get_wood_listing_of(self, worker_id):
        return self.wood_market.get_listing_of(worker_id)
    
    def get_weapon_listing_of(self, worker_id):
        return self.weapon_market.get_listing_of(worker_id)
    
    def buy_food(self):
        return self.food_market.purchase()
    
    def buy_wood(self):
        return self.wood_market.purchase()
    
    def buy_weapon(self):
        return self.weapon_market.purchase()

    def prune_listings(self, id):
        if id in self.food_market.listings.keys():
            self.food_market.listings.pop(id)
        if id in self.wood_market.listings.keys():
            self.wood_market.listings.pop(id)
        if id in self.weapon_market.listings.keys():
            self.weapon_market.listings.pop(id)