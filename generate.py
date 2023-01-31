import pyrosim.pyrosim as pyrosim

# default size variables
length = 1
width = 1
height = 1

# default position variables
x = 0
y = 0
z = 0.5

# Create world function
def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[3,5,0.5] , size=[length, width, height])
	pyrosim.End()

# Create Robot Function 
def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	
	# FIRST LINK TORSO
	pyrosim.Send_Cube(name = "Torso", pos=[0,0,2] , size=[length, width, height])	
	
	# FIRST JOINT between TORSO and BACKLEG
	pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [1,0,0.5])
	
	# BACKLEG
	pyrosim.Send_Cube(name = "Backleg", pos=[0,0,0.5] , size=[length, width, height])
	
	# JOINT BETWEEN TORSO AND FRONTLEG
	pyrosim.Send_Joint(name = "Torso_Frontleg" , parent = "Torso" , child = "Frontleg" , type = "revolute", position = [-1,0,0.5])

	# FRONTLEG
	pyrosim.Send_Cube(name = "Frontleg", pos=[0,0,0.5] , size=[length, width, height])
	
	pyrosim.End()


# Call functions
Create_World()

Create_Robot()
