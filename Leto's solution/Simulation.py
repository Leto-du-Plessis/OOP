import numpy.random as rand
import Worker
import Market

# config

num_days = 10000
num_workers = 100

class Simulation:

    next_worker_id = 0

    def __init__(self, num_days: int = num_days, num_workers: int = num_workers):

        self.num_days = num_days 
        self.workers = {
            self.next_worker_id + i: Simulation.generate_worker()
            for i in range(num_workers)
        }
        self.next_worker_id += num_workers
        self.market = Market.Market()

    def generate_worker():

        worker_type = rand.choice([0,1,2], p=[0.5, 0.3, 0.2])
        if worker_type == 0:
            return Worker.Food_Gatherer()
        if worker_type == 1:
            return Worker.Lumberjack()
        if worker_type == 2:
            return Worker.Blacksmith()
        
    def count_jobs(self):

        food_gatherers = 0
        lumberjacks = 0
        blacksmiths = 0
        for worker in self.workers.values():
            if worker.type == "food gatherer":
                food_gatherers += 1
            elif worker.type == "lumberjack":
                lumberjacks += 1
            else:
                blacksmiths += 1
        return [food_gatherers, lumberjacks, blacksmiths]

    def update(self):

        self.num_days -= 1
        dead_worker_keys = []
        new_workers = 0
    
        for key in self.workers.keys():
            worker = self.workers[key]
            if worker.buy_food():
                for purchase in range(worker.buy_food()):
                    if self.market.get_food_amount() > 0 and worker.gold >= self.market.get_food_price():
                        worker.food += 1
                        food_price = self.market.get_food_price()
                        worker.gold -= food_price
                        self.workers[self.market.buy_food()].gold += food_price
            if worker.buy_wood():
                for purchase in range(worker.buy_wood()):
                    if self.market.get_wood_amount() > 0 and worker.gold >= self.market.get_wood_price():
                        worker.wood += 1
                        wood_price = self.market.get_wood_price()
                        worker.gold -= wood_price
                        self.workers[self.market.buy_wood()].gold += wood_price
            if worker.buy_weapons():
                for purchase in range(worker.buy_weapons()):
                    if self.market.get_weapon_amount() > 0 and worker.gold >= self.market.get_weapon_price():
                        worker.weapons += 1
                        weapon_price = self.market.get_weapon_price()
                        worker.gold -= weapon_price
                        self.workers[self.market.buy_weapon()].gold += weapon_price
            worker.daily_hunger()
            if worker.hunger <= 0:
                dead_worker_keys.append(key)
                continue
            worker.eat()
            worker.gather()
            if worker.breed():
                new_workers += 1
            worker.robbery()
            sell_food = worker.sell_food(self.market.get_food_price())
            if sell_food:
                self.market.set_food_listing({key: sell_food})
            sell_wood = worker.sell_wood(self.market.get_wood_price())
            if sell_wood:
                self.market.set_wood_listing({key: sell_wood})
            sell_weapons = worker.sell_weapons(self.market.get_weapon_price())
            if sell_weapons:
                self.market.set_weapon_listing({key: sell_weapons})
    
        for key in dead_worker_keys:
            self.workers.pop(key)
            self.market.prune_listings(key)

        for i in range(new_workers):
            self.workers.update({self.next_worker_id: Simulation.generate_worker()})
            self.next_worker_id += 1

        if self.num_days%5 == 0:
            jobs = self.count_jobs()
            print(f"Day: {num_days - self.num_days}, Workers: {sum(jobs)}, Farmers: {jobs[0]}, Lumberjacks: {jobs[1]}, Blacksmiths: {jobs[2]}, Food: {self.market.get_food_amount()} @ ${self.market.get_food_price()}, Wood: {self.market.get_wood_amount()} @ ${self.market.get_wood_price()}, Weapons: {self.market.get_weapon_amount()} @ ${self.market.get_weapon_price()}.")