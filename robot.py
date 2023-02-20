#robot
import sensor as SENSORS 
import motor as MOTORS
import generate
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math
import constants as c

class ROBOT:
    def __init__(self, robotId):
        self.sensors = {}
        self.motors = {}

        #add the robot
        self.robotId = robotId

        # backleh numpy vector
        backLegSensorValues = numpy.zeros(c.length)

        # frontleh numpy vector
        frontLegSensorValues = numpy.zeros(c.length)

        # sinusoidally varying values
        numpyStuff = numpy.linspace(0, numpy.pi*2, c.length)

        targetAnglesBackLeg = numpy.array(c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * numpyStuff + c.phaseOffsetBackLeg))
        targetAnglesFrontLeg = numpy.array(c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * numpyStuff + c.phaseOffsetFrontLeg))

        # for loop for simulation
        for i in range(c.length):
            p.stepSimulation()

        	#backleg sensor
            backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

        	#frontleg sensor
            frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

        	# motors for joints
        	#backleg
            pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBackLeg[i], maxForce = 25)

        	#front leg
        	# 1.57079632679 ==  pi/2.0 & 
            # -1.57079632679 == -pi/2.0
            pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFrontLeg[i], maxForce = 25)
            
            time.sleep(c.time)

       

