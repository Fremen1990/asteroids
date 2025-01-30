import random

from constants import BIG_ASTEROID_SCORE, SMALL_ASTEROID_SCORE, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from explosion import Explosion

import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        explosion = Explosion(self.position.x, self.position.y, self.radius)
        for container in Explosion.containers:
            container.add(explosion)

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return SMALL_ASTEROID_SCORE
        else:
            random_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = new_vector1 * 1.2
            new_asteroid_2.velocity = new_vector2

            return BIG_ASTEROID_SCORE
