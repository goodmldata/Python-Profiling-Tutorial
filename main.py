import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def visualize(simulator):
    CLR = [p.color for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot()

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
        # Zero point
        line = ax.scatter(0, 0, c=["blue"])
        # Initial data
        X = np.array([p.x for p in sim.particles])
        Y = np.array([p.y for p in sim.particles])
        line = ax.scatter(X, Y, c=CLR)
        return line,  # The comma is important!

    def animate(i):
        # We let the particle evolve for 1 timeunit(s)
        sim.evolve(1)
        X = np.array([p.x for p in sim.particles])
        Y = np.array([p.y for p in sim.particles])
        line = ax.scatter(X, Y, c=CLR)
        return line,

    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    import math
    from simulator.particle_simulator import Particle, ParticleSimulator
    p1 = Particle(0.0, 0.25, math.pi / 180, color="coral")
    p2 = Particle(0, -0.5, math.pi / 60, color="springgreen")
    sim = ParticleSimulator([p1, p2])
    visualize(sim)