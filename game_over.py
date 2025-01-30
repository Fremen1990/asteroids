import sys

import pygame

from constants import GAME_OVER_FONT_SIZE, GAME_OVER_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_OVER_MESSAGE

class GameOver:
    def __init__(self, message=GAME_OVER_MESSAGE, font_size=GAME_OVER_FONT_SIZE, color=GAME_OVER_COLOR):
        self.message = message
        self.font_size = font_size
        self.color = color

    def display(self, screen):
        font = pygame.font.Font(None, self.font_size)

        text = font.render(self.message, True, self.color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2))

        # Press "R" to restart
        subtext = font.render("Press R to Restart", True, (255,255,255))
        subtext_rect = subtext.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100))

        while True:
            screen.fill("black")
            screen.blit(text, text_rect)
            screen.blit(subtext, subtext_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return