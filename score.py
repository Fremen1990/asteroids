import pygame

from constants import SCORE_POSITION
from constants import SCORE_FONT_SIZE
from constants import SCORE_COLOR

class Score:
    def __init__(self, font_size = SCORE_FONT_SIZE, color= SCORE_COLOR, position=SCORE_POSITION):
        self.score = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.position = position

    def increment(self, points):
        self.score += points

    def draw(self,screen):
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, self.color)
        screen.blit(text_surface, self.position)

    def reset(self):
        self.score = 0