
import pygame

from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            deltaTime = clock.tick(60)
            dt = deltaTime / 1000
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()