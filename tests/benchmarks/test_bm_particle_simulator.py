import pytest


class TestBenchmarkParticleSimulator:
    def test_evolve(self, configurable_simulator, benchmark):
        benchmark(configurable_simulator.evolve, 0.1)
