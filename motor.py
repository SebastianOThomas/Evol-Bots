#motor
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    # prep to act
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.offset = c.phaseOffset

        if("Back" in str(self.jointName)):
            self.frequency = c.frequency
            print("1 -----")
        else:
            print("2 -----")
            self.frequency = c.frequency * 2

         # sinusoidally varying values
        numpyStuff = numpy.linspace(0, numpy.pi*2, c.length)
        self.targetAngles = numpy.array(self.amplitude * numpy.sin(self.frequency * numpyStuff + self.offset))

    def Set_Value(self, t, ID):
        # motors for joints
    	#backleg
        pyrosim.Set_Motor_For_Joint(
          bodyIndex = ID, 
          jointName = self.jointName, 
          controlMode = p.POSITION_CONTROL, 
          targetPosition = self.targetAngles[t], 
          maxForce = 25)

        def Save_Values(self):
            pass
       

        