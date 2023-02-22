#sensor
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math
import constants as c
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        # create vector of zeros
        self.values = numpy.zeros(c.length)


    def Get_Value(self, t):
        #backleg sensor
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        print(self.values)

    def Save_Values(self): #change later if needed
        numpy.save(os.path.join("data", "backLegSensorValues.npy"), backLegSensorValues)
        numpy.save(os.path.join("data", "frontLegSensorValues.npy"), frontLegSensorValues)