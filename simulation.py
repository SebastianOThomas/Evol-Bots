from world import WORLD
from robot import ROBOT
from sensor import SENSOR
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
        physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)  # add gravity
        self.world = WORLD()
        self.robot = ROBOT()


        
        self.world = p.loadSDF("world.sdf")
       
       
        # prep bot to sense
        ROBOT.Prepare_To_Sense(self)

    def RUN(self):
         # for loop for simulation
        for i in range(c.length):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)

            time.sleep(c.time)
            print(i)

    # deconstructor
    def __del__(self):
        p.disconnect()
            


        
        
        
        

