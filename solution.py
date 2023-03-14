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


class SOLUTION:
    
    def __init__(self):
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow,randomColumn] = random.random() * (2 - 1)
        self.Create_Brain()


    def Evaluate(self, view):
        file = "python3 simulate.py " + view
        os.system(file)
        f = open("fitness.txt","r")
        self.fitness = float(f.read())
        f.close()

    # Create world function
    def Create_World(self):
        # default size variables
        length = 1
        width = 1
        height = 1

        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[3,5,0.5] , size=[length, width, height])
        pyrosim.End()

    # Create Body Function 
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # self.joint_torso_backleg_coordinates = [torso_coordinates[0]-0.5, 0, torso_coordinates[2]-(0.5*link_size[2])]
        # self.backLeg_coordinates = [link_size[0]*(-0.5),0,link_size[2]*(-0.5)]
        # self.joint_torso_frontleg_coordinates = [torso_coordinates[0]+0.5, 0, torso_coordinates[2]-(0.5*link_size[2])]
        # self.frontLeg_coordinates = [link_size[0]*0.5,0,link_size[2]*(-0.5)]

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5] , size=[1, 1, 1]) # absolute
                
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])
            
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5] , size=[1, 1, 1])
                
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])
                
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5] , size=[1, 1, 1])
                
        pyrosim.End()

    # generate brain function
    def Create_Brain(self):
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
