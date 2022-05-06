import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from functools import reduce
from math import gamma
from scipy.stats import dirichlet

corners = np.array([[0.0, 0.0], [1.0, 0], [0.5, 0.75**0.5]])
triangle = tri.Triangulation(corners[:,0], corners[:,1])

refiner = tri.UniformTriRefiner(triangle)
trimesh = refiner.refine_triangulation(subdiv=4)

plt.figure(figsize=(8,4))
for (i,mesh) in enumerate([triangle, trimesh]):
    plt.subplot(1,2,i+1)
    plt.triplot(mesh)
    plt.axis('equal')
    plt.axis('off')

midpoints = [corners[(i + 1)%3] + corners[(i + 2)%3] / 2  for i in range(3)]

def xy2abc(xy, tol=1e-10):
    """ Convert 2D Cartesian coordinates to barycentric"""
    s = [(corners[i] - midpoints[i]).dot(xy - midpoints[i]) / 0.75 for i in range(3)]
    return np.clip(s, tol, 1.0 -tol)

class Dir(object):
    def __init__(self, alpha):
        from math import gamma
        from operater import mul
        self._alpha = np.array(alpha)
        self._coef = gamma(np.sum(self._alpha)) / reduce(mul, [gamma(a) for a in self._alpha])
    def pdf(self, x):
        return self._coef * reduce(mul, [xx ** (aa-1) for (xx, aa) in zip(x, self._alpha)])
    
def draw_pdf(dist, nlevels=200, subdiv=8, **kwargs):
    import math
    refiner = tri.UniformTriRefiner(triangle)
    trimesh = refiner.refine_triangulation(subdiv=subdiv)
    pvals = [dist.pdf(xy2abc(xy)) for xy in zip(trimesh.x, trimesh.y)]
    plt.tricontourf(trimesh, pvals, nlevels, **kwargs)
    plt.axis('equal')
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.axis('off')

