
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

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    running = True
    dt = 0

    while running:
        for event in pygame.event.get():

            screen.fill("black")

            player.update(dt)

            player.draw(screen)

            pygame.display.flip()

            deltaTime = clock.tick(60)
            dt = deltaTime / 1000

            if event.type == pygame.QUIT:
                running = False



if __name__ == "__main__":
    main()