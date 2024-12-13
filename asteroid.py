import pygame
from circleshape import *
from constants import *
from main import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)   
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity*dt
    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = velocity1 * 1.2
            asteroid_2.velocity = velocity2 * 1.2