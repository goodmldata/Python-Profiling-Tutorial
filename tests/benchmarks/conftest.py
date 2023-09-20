import math
import pytest
from random import uniform
from simulator.particle_simulator import Particle, ParticleSimulator


@pytest.fixture(scope="function", params=[10, 100, 1000])
def configurable_simulator(request):
    n = request.param
    particles = [Particle(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)) for _ in range(n)]
    return ParticleSimulator(particles)
