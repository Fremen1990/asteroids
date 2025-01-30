import math
import random

from constants import BIG_ASTEROID_SCORE, SMALL_ASTEROID_SCORE, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from explosion import Explosion

import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.lumpiness = random.uniform(0.1, 0.3)
        self.points = self.generate_lumpy_shape()

    def generate_lumpy_shape(self):
        points = []
        num_points = random.randint(8, 16)  # Ensure at least 3 points
        angle_step = 360 / num_points  # Divide the circle into equal parts

        for i in range(num_points):
            angle = angle_step * i
            angle_rad = math.radians(angle)

            # Generate a random distance variation (lumpiness effect)
            offset = random.uniform(-self.radius * self.lumpiness, self.radius * self.lumpiness)

            # Calculate x, y position with lumpiness
            x = self.position.x + (self.radius + offset) * math.cos(angle_rad)
            y = self.position.y + (self.radius + offset) * math.sin(angle_rad)

            points.append((x, y))

        # 🛠 Ensure we have at least 3 points
        if len(points) < 3:
            print("⚠ Warning: Asteroid shape generated with too few points! Regenerating...")
            return self.generate_lumpy_shape()

        return points

    def draw(self, screen):
        if len(self.points) < 3:
            print("⚠ Warning: Not enough points to draw asteroid! Skipping draw.")
            return  # Skip drawing to prevent a crash

        pygame.draw.polygon(screen, "green", self.points, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.points = [(x + self.velocity.x * dt, y + self.velocity.y * dt) for x, y in self.points]

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
