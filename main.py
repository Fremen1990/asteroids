
import pygame
import sys

from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid

from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)


    AsteroidField.containers = (updatable,)


    # Create player AFTER setting containers
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)
    # Create asteroid field
    asteroid_field = AsteroidField()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic (outside event loop!)
        screen.fill("black")

        # Update all sprites
        for sprite in updatable:
                sprite.update(dt)

        # Add collision detection
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        for shot in shots:
            shot.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.splitw()
                    shot.kill()


        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        for shot in shots:
            shot.draw(screen)

        pygame.display.flip()

        deltaTime = clock.tick(60)
        dt = deltaTime / 1000



if __name__ == "__main__":
    main()