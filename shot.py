import pygame
from circleshape import *
from constants import *
from main import *
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = SHOT_RADIUS
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity*dt


