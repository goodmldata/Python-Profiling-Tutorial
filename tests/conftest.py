import math
import pytest
from simulator.particle_simulator import Particle, ParticleSimulator


@pytest.fixture
def particle_simulator():
    p1 = Particle(0, 0.25, math.pi / 180, color="lightgreen")
    p2 = Particle(0, 0.50, math.pi / 90, color="darksteelblue")
    p3 = Particle(0, 0.75, math.pi / 60, color="lightgreen")
    return ParticleSimulator([p1, p2, p3])
