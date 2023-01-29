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
	# Torso code
	pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length, width, height])	
	# Joint between torso and leg
	pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [?,?,?])
	# Leg Link
	pyrosim.Send_Cube(name="Leg", pos=[1,0,1.5] , size=[length, width, height])
	pyrosim.End()


# Call functions
Create_World()

Create_Robot()
