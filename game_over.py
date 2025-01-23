import pygame

from asteroids.constants import GAME_OVER_FONT_SIZE, GAME_OVER_COLOR
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_OVER_MESSAGE

class GameOver:
    def __init__(self, message=GAME_OVER_MESSAGE, font_size=GAME_OVER_FONT_SIZE, color=GAME_OVER_COLOR):
        self.message = message
        self.font_size = font_size
        self.color = color

    def display(self, screen):
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.message, True, self.color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2))

        screen.fill("black")
        screen.blit(text, text_rect)
        pygame.display.flip()

        pygame.time.wait(3000)

        # TODO implement - Restart functionality