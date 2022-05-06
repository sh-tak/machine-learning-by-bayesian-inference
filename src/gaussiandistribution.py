import matplotlib.pyplot as plt
import numpy as np
import math

class GaussianDistribution:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
    def _gaussfunc(self, x):
        return 1.0 / np.sqrt(2 * np.pi * self.sigma**2) * np.exp(-x**2 / (2 * self.sigma**2))
    def gaussfunc_array(self, x_array):
        return [self._gaussfunc(x) for x in x_array]
    def kl_divergence(self, p):
        return 0.5 * (p.mu**2 - 2*p.mu*self.mu + self.mu**2 + self.sigma**2 )/p.sigma**2 + math.log(p.sigma) - math.log(self.sigma) -0.5
    def draw(self):
        x = np.linspace(-10, 10, 1000)
        plt.plot(x, self.gaussfunc_array(x))
        plt.show()
    
sample1 = GaussianDistribution(0.0, 2.0)
sample2 = GaussianDistribution(2.0, 1.0)

print(sample1.kl_divergence(sample2))