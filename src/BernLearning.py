import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import scipy.stats as stats
from betadistribution import BetaDistribution

#generate 50 samples from bernoulli distribution, whose truth value of \mu is 0.25
n_sample = 50
mu_truth = 0.25
x = stats.bernoulli.rvs(mu_truth,size=n_sample)


#initialize alpha and beta, which are the parameters of beta distribution
alpha, beta = 1000, 1000 

#make a three-dimensional figure
#The left one is prior distribution. The middle one is animation. The right one is the  posterior distribution.
fig, ax = plt.subplots(ncols=3, nrows=1)
mu = np.linspace(0.001, 0.999, 500)
ims = []
fig.suptitle(r'$\alpha$=1000, $\beta$=1000')

#draw the prior distribution on the left
ax[0].plot(mu, BetaDistribution(alpha, beta).betafunc_array(mu))
ax[0].set_title('Prior Distribution')
ax[0].set_xlabel('$\mu$')
#learn parameter \mu from samples. use beta distribution as prior
for i in range(n_sample):
    if x[i]:
        alpha += 1
    else:
        beta += 1
    #update beta distribution
    beta_dist = BetaDistribution(alpha, beta).betafunc_array(mu)
    im = ax[1].plot(mu,beta_dist)
    ax[1].set_xlabel('$\mu$')
    ims.append(np.array(im))

ax[2].plot(mu, BetaDistribution(alpha, beta).betafunc_array(mu))
ax[2].set_title('Posterior Distribution')
ax[2].set_xlabel('$\mu$')
ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save('BernoulliLearning2.gif', writer='imagemagick')