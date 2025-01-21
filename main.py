
import pygame

from player import Player

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

    Player.containers = (updatable, drawable)


    # Create player AFTER setting containers
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

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

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        deltaTime = clock.tick(60)
        dt = deltaTime / 1000



if __name__ == "__main__":
    main()