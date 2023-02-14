import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math

# Variables 
length = 1000
amplitude = (numpy.pi/4)
frequency = 1
phaseOffset = 0

physicsClient = p.connect(p.GUI)

p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)


p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add gravity
p.setGravity(0,0,-9.8)

# add the floor
planeId = p.loadURDF("plane.urdf")

#add the robot
robotId = p.loadURDF("body.urdf")

# additional pyrosim setup
pyrosim.Prepare_To_Simulate(robotId)

# backleh numpy vector
backLegSensorValues = numpy.zeros(length)

# frontleh numpy vector
frontLegSensorValues = numpy.zeros(length)

# sinusoidally varying values
# targetAngles = numpy.linspace(-0.78539816339, 0.78539816339, 201)
#targetAngles = numpy.linspace(-51.7575, 51.7575, length)
numpyStuff = numpy.linspace(0, numpy.pi*2, length)
targetAngles = numpy.array(numpy.pi/4 * numpy.sin(numpyStuff))

#second vector using amplitude, frequency, and offset



# save target angle values to file
#numpy.save(os.path.join("data", "targetAngles.npy"), targetAngles)

#save second vector that uses amplitude, frequency, and offset
numpy.save(os.path.join("data", "secondTargetAngles.npy"), secondTargetAngles)
exit()

# import box
p.loadSDF("world.sdf")
for i in range(length):
	p.stepSimulation()

	#backleg sensor
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

	#frontleg sensor
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	# motors for joints
	#backleg
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', 
	controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], 
	maxForce = 25)

	#front leg
	# 1.57079632679 ==  pi/2.0 & 
	# -1.57079632679 == -pi/2.0
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', 
	controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], 
	maxForce = 25)
	
	time.sleep(1/240)
	print(backLegSensorValues)

#save leg sensor values to file
numpy.save(os.path.join("data", "backLegSensorValues.npy"), backLegSensorValues)
numpy.save(os.path.join("data", "frontLegSensorValues.npy"), frontLegSensorValues)


p.disconnect()


