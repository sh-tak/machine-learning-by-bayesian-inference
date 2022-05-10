import matplotlib.pyplot as plt
import numpy as np
from math import gamma
from math import lgamma
from math import log
from math import e

class BetaDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def betafunc(self, mu):
        return e**(lgamma(self.a+self.b) - lgamma(self.a) - lgamma(self.b) +(self.a-1)*log(mu) + (self.b-1)*log(1-mu))
    def betafunc_array(self,mu_array):
        return [self.betafunc(mu) for mu in mu_array]
    def draw(self):
        mu = np.linspace(0.001, 0.999, 1000)
        plt.plot(mu, self.betafunc_array(mu))
        plt.show()
    