#robot
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

class ROBOT:

    def __init__(self):
        #add the robot
        self.robotId = p.loadURDF("body.urdf")
        # additional pyrosim setup
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        #create neural network
        self.nn = NEURAL_NETWORK("brain.nndf")

    #prep to sense method
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    # sense method        
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t) 
    
    # prep to act
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                # get joint name
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                #get desired angle
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[neuronName].Set_Value(desiredAngle, self.robotId)

                print(neuronName)
                for i in self.motors:
                    self.motors[i].Set_Value(t, self.robotId)

    def Think(self):
        self.nn.Update()
        self.nn.Print()