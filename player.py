import pygame
from pygame.transform import rotate

from asteroids.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import PLAYER_COLOR
from constants import PLAYER_WIDTH
# from constants import PLAYER_LIVES
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot

from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y, shots):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots
        self.shoot_timer = 0
        # self.lives = PLAYER_LIVES
        self.is_invulnerable = False
        self.invulnerable_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if self.is_invulnerable:
            if pygame.time.get_ticks() % 500 <  250:
                pygame.draw.polygon(screen,PLAYER_COLOR, self.triangle(), PLAYER_WIDTH)
        else:
            pygame.draw.polygon(screen,PLAYER_COLOR, self.triangle(), PLAYER_WIDTH)

    def rotate(self, dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.is_invulnerable:
            self.invulnerable_timer -= dt
            if self.invulnerable_timer <= 0:
                self.is_invulnerable = False

        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shoot_timer >0:
                return
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            self.shoot()

    def lose_life(self):
        # self.lives -= -1
        self.respawn()

    def respawn(self):
        self.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.rotation = 0
        self.is_invulnerable = True
        self.invulnerable_timer = 3

    def move(self, dt):
        forward = pygame.Vector2(0,-1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0,-1)
        velocity = forward.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity  = velocity

        self.shots.add(shot)
