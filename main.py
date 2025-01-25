import pygame
import sys

from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from explosion import Explosion

from score import Score
from lives import Lives
from game_over import GameOver

from constants import *


def main():
    while True:  # Allow restarting the game after Game Over
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
        explosions = pygame.sprite.Group()

        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        Explosion.containers = (explosions,)

        # Create score
        score = Score()

        # Create lives
        lives = Lives(initial_lives=PLAYER_LIVES)

        # Create game over screen
        game_over_screen = GameOver()

        # Create player AFTER setting containers
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
        # Create asteroid field
        asteroid_field = AsteroidField()

        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # running = False
                    pygame.quit()
                    sys.exit()

            # Game logic (outside event loop!)
            screen.fill("black")

            # Update all sprites
            for sprite in updatable:
                sprite.update(dt)

            # Add collision detection
            for asteroid in asteroids:
                if asteroid.collision(player):
                    if not player.is_invulnerable:
                        lives.decrement()
                        player.lose_life()

                        if lives.lives <= 0:
                            print("Game over!")
                            game_over_screen.display(screen)
                            # pygame.quit()
                            # sys.exit()
                            running = False

            for shot in shots:
                shot.update(dt)

            for asteroid in asteroids:
                for shot in shots:
                    if shot.collision(asteroid):
                        explosion = Explosion(asteroid.position.x, asteroid.position.y, asteroid.radius)
                        explosions.add(explosion)

                        score_for_asteroid_hit = asteroid.split()
                        score.increment(score_for_asteroid_hit)
                        shot.kill()

            for explosion in explosions:
                explosion.update(dt)
                if explosion.finished:
                    explosions.remove(explosion)

            # Draw all sprites
            for sprite in drawable:
                sprite.draw(screen)

            for shot in shots:
                shot.draw(screen)

            for explosion in explosions:
                explosion.draw(screen)

            score.draw(screen)
            lives.draw(screen)

            pygame.display.flip()

            deltaTime = clock.tick(60)
            dt = deltaTime / 1000


if __name__ == "__main__":
    main()
