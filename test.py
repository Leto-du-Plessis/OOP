import Worker
import Simulation

farmer = Worker.Food_Gatherer()
lumberjack = Worker.Lumberjack()
blacksmith = Worker.Blacksmith()

workers = [farmer, lumberjack, blacksmith]

for worker in workers:
    print(worker.hunger, worker.food, worker.wood, worker.weapons)

print("")

for worker in workers:
    worker.gather()
    print(worker.hunger, worker.food, worker.wood, worker.weapons)

simulation = Simulation.Simulation()

while simulation.num_days >= 0:
    simulation.update()