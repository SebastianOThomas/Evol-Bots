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
    def __init__(self, directOrGUI, solutionID):
        #create simulation
        self.directOrGUI = directOrGUI
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
         
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)  # add gravity

        self.world = WORLD(solutionID)
        self.robot = ROBOT(solutionID)
       
       
        # prep bot to sense
        ROBOT.Prepare_To_Sense(self)

    # deconstructor
    def __del__(self):
        p.disconnect()


    def RUN(self):
         # for loop for simulation
        for i in range(c.length):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if (self.directOrGUI == "GUI"):
                time.sleep(c.time)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    
            


        
        
        
        

