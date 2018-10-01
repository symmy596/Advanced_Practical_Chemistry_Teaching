import numpy as np
from pylj import md, sample


def pbc():
    number_of_particles = 1
    temperature = 100
    box_length = 30
    number_of_steps = 10000
    sample_frequency = 25
    # Initialise the system
    system = md.initialise(number_of_particles, temperature, box_length,
                           'square')
    system.particles['xvelocity'] = (np.random.randn() - 0.5) * 14
    system.particles['yvelocity'] = (np.random.randn() - 0.5) * 14
    # This sets the sampling class
    sample_system = sample.JustCell(system)
    # Start at time 0
    system.time = 0
    # Begin the molecular dynamics loop
    for i in range(0, number_of_steps):
        # At each step, calculate the forces on each particle and get
        # acceleration
        system.compute_force()
        # Run the equations of motion integrator algorithm
        system.integrate(md.velocity_verlet)
        # Sample the thermodynamic and structural parameters of the system
        system.md_sample()
        # Allow the system to interact with a heat bath
        system.heat_bath(temperature)
        # Iterate the time
        system.time += system.timestep_length
        system.step += 1
        # At a given frequency sample the positions and plot the RDF
        if system.step % sample_frequency == 0:
            sample_system.update(system)
