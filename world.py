#world
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math
import constants as c

class WORLD:
    def __init__(self):
        # import box
        self.world = p.loadSDF("world.sdf")
        # add the floor
        self.planeId = p.loadURDF("plane.urdf")
