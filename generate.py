import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("tower.sdf")

# default size variables
length = 1
width = 1
height = 1

# default position variables
x = 0
y = 0
z = 0.5

# for loop for tower
for k in range(10):
	pyrosim.Send_Cube(name="Box1", pos=[x,y,z] , size=[length, width, height])
	# increase height by 1
	z += 1
			
	# adding shrinking effect
	length = length * 0.9
	width = width * 0.9
	height = height * 0.9
	
	for x in range(5):
		pyrosim.Send_Cube(name="Box1", pos=[x,y,z] , size=[length, width, height])
		x += 1
		for y in range(5):
			pyrosim.Send_Cube(name="Box1", pos=[x,y,z] , size=[length, width, height])
			y += 1

pyrosim.End()
