import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import scipy.stats as stats
from gammadistribution import GammaDistribution

#generate 50 samples from poisson distribution, whose truth value of \lambda is 0.25
n_sample = 50
lambda_truth = 2
x = np.random.poisson(lambda_truth,size=n_sample)

#initialize alpha and beta, which are the parameters of beta distribution
a, b = 4, 4

#make a three-dimensional figure
#The left one is prior distribution. The middle one is animation. The right one is the  posterior distribution.
fig, ax = plt.subplots(ncols=3, nrows=1)
mu = np.linspace(0, 5, 500)
ims = []
fig.suptitle('a= 4.0, b=4.0')

#draw the prior distribution on the left
ax[0].plot(mu, GammaDistribution(a, b).gammafunc_array(mu))
ax[0].set_title('Prior Distribution')
ax[0].set_xlabel('$\lambda$')
#learn parameter \mu from samples. use beta distribution as prior
for i in range(n_sample):
    a += x[i]
    b += 1
        #update beta distribution
    gamma_dist = GammaDistribution(a, b).gammafunc_array(mu)
    im = ax[1].plot(mu,gamma_dist)
    ax[1].set_xlabel('$\lambda$')
    ims.append(np.array(im))

ax[2].plot(mu, GammaDistribution(a, b).gammafunc_array(mu))
ax[2].set_title('Posterior Distribution')
ax[2].set_xlabel('$\lambda$')
ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save('PoissonLearning1.gif', writer='imagemagick')
