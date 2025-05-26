class Worker:
    def __init__(self, eat, int):
        self.eat = eat


class Framer(Worker):
    def __init__(self, eat: int, produce_food: int):
        super().__init__(eat)
        self.produce_food = produce_food

class Lumberjack(Worker):
    def __init__(self, eat: int, produce_wood: int):
        super().__init__(eat)
        self.produce_wood = produce_wood

class Blacksmith(Worker):
    def __init__(self, eat: int, use_resource: int, produce_weapon: int):
        super().__init__(eat)
        self.use_resource = use_resource
        self.produce_weapon = produce_weapon
        
