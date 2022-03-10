import numpy as np
import random
from math import inf


class Particle:
    """
    Represents a particle of the Particle Swarm Optimization algorithm.
    """
    def __init__(self, lower_bound, upper_bound):
        """
        Creates a particle of the Particle Swarm Optimization algorithm.

        :param lower_bound: lower bound of the particle position.
        :type lower_bound: numpy array.
        :param upper_bound: upper bound of the particle position.
        :type upper_bound: numpy array.
        """
        self.pos = np.random.uniform(lower_bound, upper_bound)
        delta = upper_bound - lower_bound
        self.speed = np.random.uniform(-delta, delta)
        self.best_x = self.pos
        self.best_cost = -inf


class ParticleSwarmOptimization:
    """
    Represents the Particle Swarm Optimization algorithm.
    Hyperparameters:
        inertia_weight: inertia weight.
        cognitive_parameter: cognitive parameter.
        social_parameter: social parameter.

    :param hyperparams: hyperparameters used by Particle Swarm Optimization.
    :type hyperparams: Params.
    :param lower_bound: lower bound of particle position.
    :type lower_bound: numpy array.
    :param upper_bound: upper bound of particle position.
    :type upper_bound: numpy array.
    """
    def __init__(self, hyperparams, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_particles = hyperparams.num_particles
        self.w = hyperparams.inertia_weight
        self.phip = hyperparams.cognitive_parameter
        self.phig = hyperparams.social_parameter

        self.bgx = np.zeros(np.size(lower_bound))
        self.bgv = -inf

        self.counter = 0
        self.best_iteration = None
        self.best_iteration_cost = -inf

        self.particles = []
        for i in range(hyperparams.num_particles):
            self.particles.append(Particle(lower_bound, upper_bound))

    def get_best_position(self):
        """
        Obtains the best position so far found by the algorithm.

        :return: the best position.
        :rtype: numpy array.
        """
        return self.bgx

    def get_best_value(self):
        """
        Obtains the value of the best position so far found by the algorithm.

        :return: value of the best position.
        :rtype: float.
        """
        return self.bgv  # Remove this line

    def get_position_to_evaluate(self):
        """
        Obtains a new position to evaluate.

        :return: position to evaluate.
        :rtype: numpy array.
        """
        return self.particles[self.counter].pos

    def advance_generation(self):
        """
        Advances the generation of particles. Auxiliary method to be used by notify_evaluation().
        """

        particle_x = self.particles[self.counter].pos
        particle_v = self.particles[self.counter].speed
        particle_best = self.particles[self.counter].best_x
        rp = random.uniform(0, 1)
        rg = random.uniform(0, 1)
        particle_v = self.w * particle_v + self.phip * rp * (particle_best - particle_x) + \
                                             self.phig * rg * (self.bgx - particle_x)
        delta = self.upper_bound - self.lower_bound
        self.particles[self.counter].speed = particle_v.clip(min=-delta, max=delta)
        particle_x = particle_x + self.particles[self.counter].speed
        self.particles[self.counter].pos = particle_x.clip(min=self.lower_bound, max=self.upper_bound)
        # avanca contador
        self.counter += 1
        if self.counter > self.num_particles - 1:
            if self.best_iteration_cost > self.bgv:
                self.bgx = self.best_iteration
                self.bgv = self.best_iteration_cost
            self.counter = 0
            self.best_iteration = None
            self.best_iteration_cost = -inf

    def notify_evaluation(self, value):
        """
        Notifies the algorithm that a particle position evaluation was completed.

        :param value: quality of the particle position.
        :type value: float.
        """
        particle_x = self.particles[self.counter].pos
        particle_best_cost = self.particles[self.counter].best_cost
        if value > particle_best_cost:
            self.particles[self.counter].best_cost = value
            self.particles[self.counter].best_x = particle_x
        if value > self.best_iteration_cost:
            self.best_iteration_cost = value
            self.best_iteration = particle_x
        self.advance_generation()

