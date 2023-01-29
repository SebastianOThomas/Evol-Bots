import pybullet as p
import time


physicsClient = p.connect(p.GUI)
# add gravity
p.setGravity(0,0,-9.8)

# add the floor
planeId = p.loadURDF("plane.urdf")

# import box
p.loadSDF("box.sdf")
for x in range(1000):
	p.stepSimulation()
	time.sleep(1/16)
	print(x)

p.disconnect()
