import pygame

from constants import LIVES_POSITION, LIVES_ICON_SIZE, PLAYER_LIVES, LIVES_HEART_ICON_PATH

class Lives:
    def __init__(self, initial_lives = PLAYER_LIVES):
        self.lives = initial_lives

        # self.icon = pygame.Surface((LIVES_ICON_SIZE, LIVES_ICON_SIZE))
        # self.icon.fill((255,255,255))

        self.heart_icon = pygame.image.load(LIVES_HEART_ICON_PATH)
        self.heart_icon = pygame.transform.scale(self.heart_icon, (LIVES_ICON_SIZE, LIVES_ICON_SIZE))

    def decrement(self):
        self.lives -= 1

    def reset(self, lives):
        self.lives = lives

    def draw(self, screen):
        x,y = LIVES_POSITION
        for i in range(self.lives):
            # screen.blit(self.icon, (x + i * (LIVES_ICON_SIZE +10), y))
            screen.blit(self.heart_icon, (x + i * (LIVES_ICON_SIZE +10), y))