from random import uniform
from simulator.particle_simulator import Particle, ParticleSimulator


def run_benchmark():
    particles = [Particle(uniform(-1, 1), uniform(-1, 1), uniform(-1,1)) for _ in range(100)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


if __name__ == "__main__":
    run_benchmark()
    print("Running benchmark: OK")
