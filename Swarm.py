import random
import numpy as np




class Swarm():

    def __init__(self, target, target_error, n_particles,c1,c2,W):
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random() * 5, random.random() * 5])
        self.c1=c1
        self.c2=c2
        self.W=W

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()

    def fitness(self, particle):
        x1=particle.position[0]
        x2=particle.position[1]
        a = 20
        b = 0.2
        c = 2 * np.pi

        sum1 = x1 ** 2 + x2 ** 2
        sum2 = np.cos(c * x1) + np.cos(c * x2)

        term1 = - a * np.exp(-b * ((1 / 2.) * sum1 ** (0.5)))
        term2 = - np.exp((1 / 2.) * sum2)

        return term1 + term2 + a + np.exp(1)

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if (particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if (self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            new_velocity = (self.W * particle.velocity) + (self.c1 * random.random()) * (
                        particle.pbest_position - particle.position) + \
                           (random.random() * self.c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
