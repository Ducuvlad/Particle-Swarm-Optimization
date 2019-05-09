from Particle import Particle
from Swarm import Swarm


def run(target_error, n_particles,c1,c2,w,n_iterations):
    fit = []
    search_space = Swarm(1, target_error, n_particles,c1,c2,w)
    particles_vector = [Particle() for _ in range(search_space.n_particles)]
    search_space.particles = particles_vector
    #search_space.print_particles()

    iteration = 0
    while (iteration < n_iterations):
        search_space.set_pbest()
        search_space.set_gbest()

        if (abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
            break
        search_space.move_particles()
        fit.append(search_space.gbest_value)
        iteration += 1
    return (search_space.gbest_position,iteration,fit)