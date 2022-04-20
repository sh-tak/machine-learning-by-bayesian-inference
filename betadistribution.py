import matplotlib.pyplot as plt
import numpy as np
from math import gamma

class BetaDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def betafunc(self, mu):
        return [gamma(self.a+self.b) / (gamma(self.a) * gamma(self.b)) * (mu**(self.a-1)) * ((1-mu)**(self.b-1))]
    def betafunc_array(self,mu_array):
        return [self.betafunc(mu) for mu in mu_array]
    def draw(self):
        mu = np.linspace(0.001, 0.999, 1000)
        plt.plot(mu, self.betafunc_array(mu))
        plt.show()

sample = BetaDistribution(10.0, 40.0)
sample.draw()
    