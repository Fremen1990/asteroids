import random

import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        super().__init__(self.containers)  # Use only the explosions group
        self.frames = self.load_frames(size)
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x,y))
        self.animation_timer = 0.0
        self.animation_speed = 0.1
        self.finished = False

    def load_frames(self, size):
        frames = []
        for _ in range(6):
            surface = pygame.Surface((size * 2, size *2), pygame.SRCALPHA)
            pygame.draw.circle(
                surface, (255, random.randint(100, 255),0),(size, size), random.randint(size //2, size)
            )
            frames.append(surface)
        return frames

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer > self.animation_speed:
            self.animation_timer = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
            else:
                self.finished = True  # Mark the explosion as finished

    def draw(self, screen):
        if not self.finished:
            screen.blit(self.image, self.rect)