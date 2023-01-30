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
	pyrosim.Send_Cube(name="Link0", pos=[1.5,0,2.5] , size=[length, width, height])	
	
	# FIRST JOINT between TORSO and BACKLEG
	pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = 
[2,0,2])
	
	# BACKLEG
	pyrosim.Send_Cube(name="Link1", pos=[1.5,0,1.5] , size=[length, width, height])
	
	
	pyrosim.End()


# Call functions
Create_World()

Create_Robot()
