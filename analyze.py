import numpy
import matplotlib.pyplot as plot
import os
#### SENSOR VALUES
# load sensor values into vector
# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)

# backLegSensorValues = numpy.load(os.path.join("data", "backLegSensorValues.npy"))
# frontLegSensorValues = numpy.load(os.path.join("data", "frontLegSensorValues.npy"))

# print(backLegSensorValues)
# print(frontLegSensorValues)

# #graph stuff
# plot.plot(backLegSensorValues, label = "Back Leg", linewidth = 5)
# plot.plot(frontLegSensorValues, label = "Front Leg")

# #legends
# plot.legend(loc = "upper right")
# #graph
#plot.show()


#### TARGET ANGLES
# load values into vector
# targetAngles = numpy.zeros(1000)
# targetAngles = numpy.load(os.path.join("data", "targetAngles.npy"))
# #plot
# plot.plot(numpy.arange(len(targetAngles)), targetAngles, label = "target angles")
# plot.xlabel("Steps")
# plot.ylabel("Value in Radians")
# plot.legend()

# plot.show()

#### SECOND VEC WITH AMPLITUDE FREQUENCY AND OFFSET
targetAnglesFrontLeg = numpy.load(os.path.join("data", "targetAnglesFrontLeg.npy"))
targetAnglesBackLeg = numpy.load(os.path.join("data", "targetAnglesBackLeg.npy"))

#plot
plot.plot(numpy.arange(len(targetAnglesFrontLeg)), targetAnglesFrontLeg, label = "targetAnglesFrontLeg")
plot.plot(numpy.arange(len(targetAnglesBackLeg)), targetAnglesBackLeg, label = "targetAnglesBackLeg")
plot.show()