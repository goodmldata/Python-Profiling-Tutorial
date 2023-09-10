class Particle:
    def __init__(self, x, y, ang_vel, color="red"):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel
        self.color = color


class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 10**(-4)
        nsteps = int(dt/timestep)
        for i in range(nsteps):
            for p in self.particles:
                dx = - p.ang_vel * p.y * timestep
                dy = p.ang_vel * p.x * timestep
                p.x += dx
                p.y += dy

