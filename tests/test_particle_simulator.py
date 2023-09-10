from pytest import approx

rel = 10**(-3)
eps = 10**(-6)


class TestParticleSimulator:
    def test_evolve_00(self, particle_simulator):
        particle_simulator.evolve(0)
        particles = particle_simulator.particles
        for p in particles:
            assert p.x == approx(p.x, rel=rel, abs=eps)
            assert p.y == approx(p.y, rel=rel, abs=eps)

    def test_evolve_90(self, particle_simulator):
        particle_simulator.evolve(90)
        p1, p2, p3 = particle_simulator.particles

        assert p1.x == approx(-0.25, rel=rel, abs=eps)
        assert p1.y == approx(0, rel=rel, abs=eps)

        assert p2.x == approx(0, rel=rel, abs=eps)
        assert p2.y == approx(-0.5, rel=rel, abs=eps)

        assert p3.x == approx(0.75, rel=rel, abs=eps)
        assert p3.y == approx(0, rel=rel, abs=eps)
