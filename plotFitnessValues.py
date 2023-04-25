# plot stuff
import matplotlib.pyplot as plot
import numpy

quadFitness = []
hexaFitness = []
hexaFitness = numpy.load("Fitness Values Quad.npy")
quadFitness = numpy.load("Fitness Values Hexa.npy")


plot.plot(quadFitness[:,0], label = "quadFitness")
plot.plot(hexaFitness[:,0], label = "hexaFitness")
plot.xlabel("Generation Number")
plot.ylabel("Fitness Value")
plot.legend()
plot.title("Quad v. Hexa Pod (15 Generations)")
plot.show()