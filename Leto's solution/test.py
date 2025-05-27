import Worker
import Simulation

simulation = Simulation.Simulation()

while simulation.num_days >= 0:
    simulation.update()