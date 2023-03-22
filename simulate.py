from simulation import SIMULATION
import sys


# call the simulation class
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)


#call run function 
simulation.RUN()

simulation.Get_Fitness()


