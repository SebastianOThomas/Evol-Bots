from simulation import SIMULATION
import sys


# call the simulation class
directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)


#call run function 
simulation.RUN()

simulation.Get_Fitness()


