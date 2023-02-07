import numpy
import matplotlib.pyplot as plot
import os

# load files into vector
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

backLegSensorValues = numpy.load(os.path.join("data", "backLegSensorValues.npy"))
frontLegSensorValues = numpy.load(os.path.join("data", "frontLegSensorValues.npy"))

print(backLegSensorValues)
print(frontLegSensorValues)

#graph stuff
plot.plot(backLegSensorValues, label = "Back Leg", linewidth = 5)
plot.plot(frontLegSensorValues, label = "Front Leg")

#legends
plot.legend(loc = "upper right")
#graph
plot.show()
