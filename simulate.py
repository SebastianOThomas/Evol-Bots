import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math
import constants as c
from simulation import SIMULATION
from sensor import SENSOR

# call the simulation class
simulation = SIMULATION()

#call run function 
simulation.RUN()

simulation.Get_Fitness()


