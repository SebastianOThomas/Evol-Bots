import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add gravity
p.setGravity(0,0,-9.8)

# add the floor
planeId = p.loadURDF("plane.urdf")

# import box
p.loadSDF("box.sdf")
for x in range(2000):
	p.stepSimulation()
	time.sleep(1/16)
	print(x)

p.disconnect()
