from math import gamma, e, lgamma, log
import matplotlib.pyplot as plt
import numpy as np

class GammaDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gammafunc(self, lambda_):
        if lambda_ == 0: #avoid log(0)
            return 0
        else: return e**((self.a-1)*log(lambda_) - self.b*lambda_+ self.a*log(self.b) -lgamma(self.a))
    def gammafunc_array(self, lambda_array):
        return [self.gammafunc(lambda_) for lambda_ in lambda_array]
    def draw(self):
        lambda_ = np.linspace(0, 10, 1000)
        plt.plot(lambda_, self.gammafunc_array(lambda_))
        plt.show()
