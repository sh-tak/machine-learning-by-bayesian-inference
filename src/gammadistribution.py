from math import gamma, e
import matplotlib.pyplot as plt
import numpy as np

class GammaDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gammafunc(self, rambda):
        return self.b**self.a / gamma(self.a) * rambda**(self.a-1) * e**(-self.b*rambda)
    def gammafunc_array(self, rambda_array):
        return [self.gammafunc(rambda) for rambda in rambda_array]
    def draw(self):
        rambda = np.linspace(0, 10, 1000)
        plt.plot(rambda, self.gammafunc_array(rambda))
        plt.show()

sample = GammaDistribution(10.0, 40.0)
sample.draw()