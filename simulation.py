from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math
import constants as c

class SIMULATION:
    def __init__(self):
        #create simulation 
        self.physicsClient = p.connect(p.GUI)

        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # add gravity
        p.setGravity(0,0,-9.8)
        

        #add the robot
        self.robotId = p.loadURDF("body.urdf")
        self.world = p.loadSDF("world.sdf")
        
        # additional pyrosim setup
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.world = WORLD(self.world)
        self.robot = ROBOT(self.robotId)

    def RUN():
        #skill issue
        


        
        
        
        

