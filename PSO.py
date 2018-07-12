import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def target(pos):
    x, y = pos
    return x*x - 10*np.cos(2*np.pi*x) + y*y - 10*np.cos(2*np.pi*y)


class Particle:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.best_pos = None
        self.best_err = float("inf")


# Initialize the population of N particles
N = 25
particles = []
for i in range(25):
    pos = np.random.uniform(-10, 10, size=(2,))
    vel = np.random.uniform(-1, 1, size=(2,))
    particle = Particle(pos, vel)
    particles.append(particle)
best_err_g = float("inf")
best_pos_g = None
c1 = 2
c2 = 2
w = 0.8
MaxIter = 100
# Initialize figure
fig = plt.figure()
ims = []

for i in range(MaxIter):
    # Main loop
    for particle in particles:
        # Calculate the objective of the particle
        err = target(particle.pos)
        # Update PBEST if required
        if err < particle.best_err:
            particle.best_err = err
            particle.best_pos = particle.pos
        # Update GBEST if required
        if err < best_err_g:
            best_err_g = err
            best_pos_g = particle.pos

    # Updatethe inertia weight
    r1 = np.random.uniform(0, 1)
    r2 = np.random.uniform(0, 1)
    for particle in particles:
        # Update the velocity
        vel_cognitive = c1*r1*(particle.best_pos - particle.pos)
        vel_social = c2*r2*(best_pos_g - particle.pos)
        particle.vel = w*particle.vel + vel_cognitive + vel_social
        # Update the position
        particle.pos = particle.pos + particle.vel
    print("Iter:{}, best_pos:{}, target:{}".format(i, best_pos_g, target(best_pos_g)))

    # Plot particles
    plot_points = np.zeros((N, 2))
    for i, p in enumerate(particles):
        plot_points[i] = p.pos
    ims.append((plt.scatter(plot_points[:,0], plot_points[:,1]+i, c='r'),))

im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat=False,
                                   blit=True)
plt.show()