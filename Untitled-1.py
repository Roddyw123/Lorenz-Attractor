

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import SpectralEmbedding




def cords(x, y, z):

    # Change Inputs Here for Lorenz Fractcal Change
    s = 4.582
    r = 13.429
    b = 3.76

    x_derivative = s * (y - x)
    y_derivative = r * x - y - x * z
    z_derivative = x * y - b * z
    return x_derivative, y_derivative, z_derivative


dt = 0.01
num_steps = 10000

xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

xs[0], ys[0], zs[0] = (0., 1., 1.05)


for i in range(num_steps):

    x_derivative, y_derivative, z_derivative = cords(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_derivative * dt)
    ys[i + 1] = ys[i] + (y_derivative * dt)
    zs[i + 1] = zs[i] + (z_derivative * dt)

fig = plt.figure() 
graph = fig.gca(projection="3d")

graph.plot(xs, ys, zs, lw = 0.5, color="navy")
graph.scatter(xs, ys, zs, lw = 0.1, alpha = 0.1, color="yellow")
graph.set_xlabel("X-Axis")
graph.set_ylabel("Y-Axis")
graph.set_zlabel("Z-Axis")
graph.set_title("Lorenz Attractor: Mathematical Representation of the Butterfly Effect, Chaos Theory.")

plt.show()
