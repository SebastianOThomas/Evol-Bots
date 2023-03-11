#solution python file
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random as random
import math
import constants as c
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import simulate.py

class SOLUTION:
    
    def __init__(self):
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self):
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

        # Create Body Function 
        def Create_Body():
            pyrosim.Start_URDF("body.urdf")

            joint_torso_backleg_coordinates = [torso_coordinates[0]-0.5, 0, torso_coordinates[2]-(0.5*link_size[2])]
            backLeg_coordinates = [link_size[0]*(-0.5),0,link_size[2]*(-0.5)]
            joint_torso_frontleg_coordinates = [torso_coordinates[0]+0.5, 0, torso_coordinates[2]-(0.5*link_size[2])]
            frontLeg_coordinates = [link_size[0]*0.5,0,link_size[2]*(-0.5)]

            pyrosim.Send_Cube(name="Torso", pos=torso_coordinates , size=link_size) # absolute
            
            pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = joint_torso_backleg_coordinates)
            
            pyrosim.Send_Cube(name="BackLeg", pos=backLeg_coordinates , size=link_size)
            
            pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = joint_torso_frontleg_coordinates)
            
            pyrosim.Send_Cube(name="FrontLeg", pos=frontLeg_coordinates , size=link_size)
            
            pyrosim.End()

        # generate brain function
        def Create_Brain():
            pyrosim.Start_NeuralNetwork("brain.nndf")

            # send sensor neurons
            pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
            pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
            pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

            # send motor neurons
            pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
            pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

            #for loop to deal with sending synapses
            for currentRow in range(0,3):
                for currentColumn in range(0,2):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight = self.weights[currentRow][currentColumn])
            pyrosim.End()
            
        link_size = [1, 1, 1]
        torso_coordinates = [1, 0, 1.5*link_size[2]]
        # Call functions
        Create_World()
        Create_Body()
        Create_Brain()

        # run simulate.py
        # TODO FIND SOLUTION TO THIS ERROR with calling OS commands
        os.system("python3 simulate.py")


