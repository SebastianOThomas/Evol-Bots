import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os

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
backLegSensorValues = numpy.zeros(100)

# frontleh numpy vector
frontLegSensorValues = numpy.zeros(100)


# import box
p.loadSDF("world.sdf")
for i in range(100):
	p.stepSimulation()
	
	#backleg sensor
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

	#frontleg sensor
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	time.sleep(1/16)
	print(backLegSensorValues)

#save values to file
numpy.save(os.path.join("data", "backLegSensorValues.npy"), backLegSensorValues)
numpy.save(os.path.join("data", "frontLegSensorValues.npy"), frontLegSensorValues)

p.disconnect()


