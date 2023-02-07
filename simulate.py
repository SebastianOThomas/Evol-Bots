import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random

physicsClient = p.connect(p.GUI)

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
backLegSensorValues = numpy.zeros(1000)

# frontleh numpy vector
frontLegSensorValues = numpy.zeros(1000)


# import box
p.loadSDF("world.sdf")
for i in range(1000):
	p.stepSimulation()

	#backleg sensor
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

	#frontleg sensor
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	# motors for joints
	#backleg
	# 1.57079632679 ==  pi/2.0 & 
	# -1.57079632679 == -pi/2.0
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', 
	controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-1.57079632679, 1.57079632679), maxForce = 25)

	#front leg
	# 1.57079632679 ==  pi/2.0 & 
	# -1.57079632679 == -pi/2.0
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', 
	controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-1.57079632679, 1.57079632679), maxForce = 25)
	
	time.sleep(1/10)
	print(backLegSensorValues)

#save values to file
numpy.save(os.path.join("data", "backLegSensorValues.npy"), backLegSensorValues)
numpy.save(os.path.join("data", "frontLegSensorValues.npy"), frontLegSensorValues)

p.disconnect()


